# NYPD Civilian Complaint Review Board Data

A collection of data on complaints to the Civilian Complaint Review Board (CCRB) on police misconduct.

## About

### What is the CCRB? 
> The New York City Civilian Complaint Review Board (CCRB) is an independent agency. It is empowered to receive, investigate, mediate, hear, make findings, and recommend action on complaints against New York City police officers alleging the use of excessive or unnecessary force, abuse of authority, discourtesy, or the use of offensive language. The Board’s investigative staff, composed entirely of civilian employees, conducts investigations in an impartial fashion. The Board forwards its findings to the police commissioner.
Source: [CCRB Website](https://www1.nyc.gov/site/ccrb/about/about.page)

### Where is this data from?
This data is published as part of NYC's Open Data Law, signed in 2012. This law mandates that all public data sets, any data set maintained on a computer by a City agency, be made public on a single web portal. Learn more about NYC Open Data on their [website](https://opendata.cityofnewyork.us/)

### What is the goal of this repo?

A single location for storage, discussion, and data exploration on reported NYPD misconduct.

While the city does a good job of providing open data, there are several things we can improve with this approach.
1. Data sets on similar topics are spread across different listings, data sets do not have references to other related data sets, and search functionality is poor -> This is a barrier to conducting any deep dive analysis on single topics
2. The data portal is a way to access data, but has no way for members of the public to ask questions or share their findings based on their analyses -> this repository will provide a better way for analysts to talk and collaborate

---

## Dataset Descriptions
**Data Transparency Initiative** "Allegations" | [Source](https://www1.nyc.gov/site/ccrb/policy/data-transparency-initiative-allegations.page)
* Includes: Data visualizations, record level data
* Broken link: The link for complaint level data on the page is broken, but can be accessed [here](https://www1.nyc.gov/assets/ccrb/downloads/excel/ccrb_datatransparencyinitiative.xlsx).
* Misleading visualizations: While the Data Transparency Initiaitve is a good effort to present this data to the public, the way information is presented obscures important narratives. For example, data on complaints for chokeholds (a reviled practice which is banned by the NYPD and led to the death of Eric Garner) is shown next to instances of "force" (a general catch all term). Relative to this broader term, the number of chokeholds looks very small, which could lead one to believe it is not an issue. But the number and percentage of these instances is not weighted by their severity. A better visualization would be to plot a timeline of all reported cases of NYPD chokehold use separate from data about other issues.

**NYC Open Data** "Civilian Complaint Review Board (CCRB) - Complaints Received" [Source](https://data.cityofnewyork.us/Public-Safety/Civilian-Complaint-Review-Board-CCRB-Complaints-Re/63nx-cpi9)
* Includes: record level data, data dictionary

**NYC Open Data** "Civilian Complaint Review Board (CCRB) - Complaints Closed" [Source](https://data.cityofnewyork.us/Public-Safety/Civilian-Complaint-Review-Board-CCRB-Complaints-Cl/fx4z-5xg2)
* Includes: record level data, data dictionary

**NYC Open Data** "Civilian Complaint Review Board (CCRB) - Allegations Closed" [Source](https://data.cityofnewyork.us/Public-Safety/Civilian-Complaint-Review-Board-CCRB-Allegations-C/xyq2-jjkn)
* Includes: record level data, data dictionary
* Note: A complaint reffers to one or more allegations against an officer. E.g. A single complaint could allege that an officer both used a racial slur and excessive force. 

