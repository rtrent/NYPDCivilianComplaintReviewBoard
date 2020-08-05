import csv
import sqlite3

#create SQL database file
open("data/nyccrb.db", "w").close()
con = sqlite3.connect("data/nyccrb.db")
cur = con.cursor()

#create SQL tables
cur.execute("CREATE TABLE IF NOT EXISTS officers (id INTEGER PRIMARY KEY, first_name VARCHAR, last_name VARCHAR, rank_current VARCHAR, command_current VARCHAR, ethnicity VARCHAR, gender VARCHAR);")
cur.execute("CREATE TABLE IF NOT EXISTS complaints (id INTEGER PRIMARY KEY, ethnicity VARCHAR, gender VARCHAR, age INTEGER, officer_id INTEGER, officer_rank VARCHAR, precinct VARCHAR, officer_command VARCHAR, contact_reason VARCHAR, contact_outcome VARCHAR, month INTEGER, year INTEGER, FOREIGN KEY (officer_id) REFERENCES officers (id));")
cur.execute("CREATE TABLE IF NOT EXISTS allegations (id INTEGER PRIMARY KEY AUTOINCREMENT, complaint_id INTEGER, officer_id INTEGER, month INTEGER, year INTEGER, fado_type VARCHAR, fado_detail VARCHAR, FOREIGN KEY (officer_id) REFERENCES officers (id), FOREIGN KEY (complaint_id) REFERENCES complaints (id));")
cur.execute("CREATE TABLE IF NOT EXISTS investigations (id INTEGER PRIMARY KEY, month_closed INTEGER, year_closed INTEGER, board_disposition VARCHAR);")


#open csv of data provided by ProPublica
with open("data/allegations_20200726939.csv", "r") as allegations:

    #read as a dictionary
    reader = csv.DictReader(allegations)

    #in each row, parse information and save as a distinct variable to use later in the SQL commands to make rows
    for row in reader:
        #data on the substance of each allegation, basic ids, what kind of violation, when did it happen
        officer_id = row['unique_mos_id']
        complaint_id = row['complaint_id']
        month = row['month_received']
        year = row['year_received']
        fado_type = row['fado_type']
        fado_detail = row['allegation']

        #more detailed data on each complaint - who the complainant was and info about the officer at that time
        rank_incident = row['rank_incident']
        contact = row['contact_reason']
        outcome = row['outcome_description']
        officer_age = row['mos_age_incident']
        complainant_ethnicity = row['complainant_ethnicity']
        complainant_gender = row['complainant_gender']
        complainant_age = row['complainant_age_incident']
        precinct = row['precinct']
        command_incident = row['command_at_incident']

        #data on each officer, name, current rank, current command
        rank_now = row['rank_now']
        officer_ethnicity= row['mos_ethnicity']
        command_now = row['command_now']
        first = row['first_name']
        last = row['last_name']
        officer_gender = row['mos_gender']
        officer_ethnicity = row['mos_ethnicity']

        #data on the investigations and decisions by the CCRB
        month_closed = row['month_closed']
        year_closed = row['year_closed']
        board_disposition = row['board_disposition']

        #insert information into a new row of each database
        cur.execute("INSERT OR IGNORE INTO officers (id, first_name, last_name, rank_current, command_current, ethnicity, gender) VALUES(?,?,?,?,?,?,?)", (officer_id, first, last, rank_now, command_now, officer_ethnicity, officer_gender))
        cur.execute("INSERT OR IGNORE INTO complaints (id, ethnicity, gender, age, officer_id, officer_rank, precinct, officer_command, contact_reason, contact_outcome, month, year) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", (complaint_id, complainant_ethnicity, complainant_gender, complainant_age, officer_id, rank_incident, precinct, command_incident, contact, outcome, month, year))
        cur.execute("INSERT INTO allegations (complaint_id, officer_id, month, year, fado_type, fado_detail) VALUES(?, ?, ?, ?, ?, ?)", (complaint_id, officer_id, month, year, fado_type, fado_detail))
        cur.execute("INSERT OR IGNORE INTO investigations (id, month_closed, year_closed, board_disposition) VALUES(?,?,?,?)", (complaint_id, month_closed, year_closed, board_disposition))

#close files
con.commit()
con.close()