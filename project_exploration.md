#### Exploratory Data Munging and Visualization
#### Analysis of Emergency Response Times
#### Sai Ganesh Nindra
#### 10/22/2024

## Basic Questions
**Dataset Author(s):** Police Department (NYPD)
**Dataset Construction Date:** November 10, 2020
**Dataset Last Updated** :- July 22, 2024
**Dataset Record Count:** 3,644,715
**Dataset File Hash(es):** 62ccdf8178fbcdfe77feba655d9c76a2
**Dataset Field Meanings:** 

CAD_EVNT_ID :- ID of the Event (Text)
CREATE_DATE :- Date of Call (Timestamp)
INCIDENT_DATE :- Date of Incident (Timestamp)
INCIDENT_TIME :- Time of Incident (Text)
NYPD_PCT_CD :- Precinct that recieved the call (Number)
BORO_NM :- Borough the call is in (Text)
PATRL_BORO_NM :- The patrol the borough is in (Text)
GEO_CD_X :- The X-Coordinate of the midblock of the street where the violation was issued (Text)
GEO_CD_Y :- The Y-Coordinate of the midblock of the street where the violation was issued (Text)
RADIO_CODE :- The code to inform a NYPD member (Text)
TYP_DESC :- Description based on Radio Code (Text)
CIP_JOBS :- Flag indicating if it is a Crime in Progress (Text)
ADD_TS :- Timestamp of when the call was added (Timestamp)
DISP_TS :- Timestamp of when the unit was dispatched (Timestamp)
ARRIVD_TS :- Timestamp of when the unit arrived on scene (Timestamp)
CLOSNG_TS :- Timestamp of when the call was closed (Timestamp)
Latitude :- Latitude of the midblock of the street where the violation was issued (Number)
Longitude :- Longitude of the midblock of the street where the violation was issued (Number)

URL :- https://data.cityofnewyork.us/Public-Safety/NYPD-Calls-for-Service-Year-to-Date-/n2zq-pubd/about_data
Click export and download the data set 

**Dataset Author(s):** Open Meteo
**Dataset Construction Date:** Updated daily, can access data from 1940 to present 
**Dataset Record Count:** 720
**Dataset File Hash(es):** 
MD5 hash of Bronx.csv : 4fe83166c3191e16c90383e9152ca29f
MD5 hash of Brooklyn.csv : 8214bfa144c327c3441391c3e203c9a0
MD5 hash of Manhattan.csv : 0bdf3033e0680939dd98261ff935532a
MD5 hash of Queens.csv : b7e2de103b0569394c4c17049534d631
MD5 hash of Staten Island.csv : 88123cc1b18e5fc00aa5d021abacb2a7
**Dataset Field Meanings:**
COLUMN DETAILS
time :- Timestamp of the day (Text)
temperature_2m (Â°C) :- Temperature in Celsius (Number)
precipitation (mm) :- Rain and Snow in mm (Number)
rain (mm) :- Rain in mm (Number)
snowfall (cm) :- Snowfall in cm (Number)
snow_depth (m) :- Depth of snowfall on ground in m (Number)

URL :- https://open-meteo.com/en/docs/historical-weather-api

## Interpretable Records
### Record 1
**Raw Data:** 
 CAD_EVNT_ID :- 	 104281501
 CREATE_DATE :-	 6/30/2024
 INCIDENT_DATE:-	 6/30/2024
 INCIDENT_TIME :-  23:59:59
 NYPD_PCT_CD :-      7
 BORO_NM	 :-    MANHATTAN
 PATRL_BORO_NM	:-  PATROL BORO MAN SOUTH
 GEO_CD_X	 :-    988309
 GEO_CD_Y	  :-   200805
 RADIO_CODE	:-     68Q1
 TYP_DESC	:-     SEE COMPLAINANT: OTHER/INSIDE
 CIP_JOBS:-	Non CIP
 ADD_TS	 :-  6/30/2024 23:59
 DISP_TS :-	6/30/2024 23:59
 ARRIVD_TS:-	6/30/2024 23:59
 CLOSNG_TS:-	7/1/2024 0:28
 Latitude:-	40.717847
 Longitude:- -73.985359
 
 **Interpretation:** 
 A call made to NYPD with ID 104281501 was created on 30th June 2024. The incident time was registered as 23:59:59. It was reported to the 7th Precinct. The incident took place in Manhattan. The patrol unit was of South Manhattan. The reported incident was a Non CIP, meaning it was not a crime in progress. The dispatch was informed at 23:59:59 and arrived at 23:59:59 which indicates a arrival time of 0's which indicates a unit being in close proximity to the incident. Indicates a good a number of patrol cars are out on the street which help in arriving on scene instantly in such cases. The GEO_CD_X refers to the X coordinate of where the call came from and GEO_CD_Y is the Y coordinate of where the call came from. The latitude and longitude correspond to the segment of the road where the incident occurred. The descripiton tells us about the situation at the site of incident here, meeting the complainant inside. 
 
### Record 2
**Raw Data:** 
 CAD_EVNT_ID :- 	 103928026
 CREATE_DATE :-	 6/16/2024
 INCIDENT_DATE:-	 6/16/2024
 INCIDENT_TIME :-  19:03:42
 NYPD_PCT_CD :-      107
 BORO_NM	 :-    QUEENS
 PATRL_BORO_NM	:-  PATROL BORO QUEENS SOUTH
 GEO_CD_X	 :-    1033110
 GEO_CD_Y	  :-   205408
 RADIO_CODE	:-     10K2
 TYP_DESC	:-    INVESTIGATE/POSSIBLE CRIME: KNIFE/OUTSIDE
 CIP_JOBS:-	Non CIP
 ADD_TS	 :-  6/16/2024 19:03
 DISP_TS :-	6/16/2024 19:07
 ARRIVD_TS:-	6/16/2024 19:15
 CLOSNG_TS:-	6/16/2024 19:19
 Latitude:-	40.730347
 Longitude:- -73.82371
 
 **Interpretation:** 
 A call was made to the NYPD and registered with ID 103928026 on 16th June 2024. 16th June 2024 is the incident time as well. 107 is the Precinct that recieved the call in Queens. Patrol intimated was the Patrol of Queens South. It was not a crime in progress. Looking at the arrival and dispatch time it seems like it took the police only 4 minutes to reach which is commendable. Quick responses from the department is whats necessary. The latitude and longitude 40.730347 and -73.82371 correspond to the location of the incident in the borough given Queens. 
 
### Record 2
**Raw Data:** 
 time 2024-06-01T00:00	
 temperature_2m (Â°C) 15.3	
 precipitation (mm)	0
 rain (mm)	0
 snowfall (cm)	0
 snow_depth (m)  0

**Interpretation:** 
The time provides the information on the hour and date of the weather at that hour. Temperature_2m indicates the temperature is in celcius. Precipitation indicates level of rain and snow at that hour in millimetre. Rain indicates the level of rain at that hour in millimetre. Snowfall indicates the level of snowfall in centimetre. Here the data tells us that on 1st June 2024 there was no rainfall or snowfall and the temperature was at 15.3 C. This when integrated with emergency data helps us analyse if calls are responded faster when there is no rainfall, snowfall and when temperature is low or high. 

## Background Domain Knowledge
911 Dispatch calls data is one of the most important thing to be optimised, this generation where crime is becoming more common we need dispatch teams to act faster than ever. Coordination between complainant, precinct call reciever and patrol unit is of utmost importance to make this process go through faster. There are definetly other factors like traffic and weather that affect the time taken for patrol units to arrive on scene.
From the article [1] The Evolution of Emergency Calls we learn that it was not until 1999 that the force could retrieve the call location, which speeds up things as there are cases where the complainant/caller does not know their location. However since reporting is still done through call, it supposedly is not the most efficient method because there are a lot Crime in Progress situations where sometimes the caller cannot speak as it will compromise their safety. 
From a New York times article [2] '911 Systems Disrupted in at Least 3 States' we gain insight on the fact that the 911 centres even though they faced outage due to the the crowdstrike situation they were up and running with reporting happening in written form. 
Sometimes being even 30 seconds earlier to a scene can help the authorities alleviate the situation and save lives or prevent said crime from happening. It is all a matter of seconds. Response time is a crucial factor in dispatch units reaching the scene as soon as possible and analysis will help us figure out. 
This article clearly tells us how important response times are, its headline is 'As Vallejo police force shrinks, 911 response times soar [3] 'Vallejo might be one case but any force/department must have enough units to respond to every call and respond as soon as possible to prevent crime. If data shows a certain amount of calls, departments must be equipped with sufficient man power to respond to the call and dispatch units for it. Lives are lost and are turned upside down within in the blink of a eye, every 911 call is important and must be attended to. The crucial factors affecting response times are usually, total number of dispatch units available to call sent to dispatch ratio, weather and traffic.

[1] https://www.tylertech.com/resources/blog-articles/the-evolution-of-emergency-calls
[2] https://www.nytimes.com/2024/07/19/business/emergency-911-calls-tech-outage.html
[3] https://openvallejo.org/2024/09/23/as-vallejo-police-force-shrinks-911-response-times-soar/

## Dataset Generality
The dataset that I have taken is representative of the real world. The extremes of weather data also exists where the rainfall has been extreme and low. There is data for every call picked up by the 911 Dispatch centre with data like when the call was accepted, when the units were dispatched and when they arrived. The time taken has also been variable indicating multiple scenarios such as when the dispatch unit is already present around the location where time taken is very less and then at times when it has taken hours for dispatch units to reach, which can be indicative of bad traffic, issues with locating the crime in progress , leaving it open to interpretation where scenarios can be of hostage too. It covers latitudes and longitudes only of New York State which I have cross verified.The borough names are also sound of real world date given that the state of New York has only 5 boroughs. The snowfall data sadly does not reflect anyting as there is no snowfall in the month of June in New York.

## Data Transformations
### Transformation 1
**Description:** Reducing Data
**Soundness Justification:** 
[1] Data Was broken down into chunks and stored into seperate csv files as the data was too much to work with. (3.64million records)

### Transformation 2
**Description:** Data integration
**Soundness Justification:** 
[2] The calls data and weather data had to be integrated on a common column.
Timestamp was chosen where i extracted date and hour of the weather data on one side and date and hour of the dispatch time. The data was integrated after dividing the calls data first into each of their boroughs. So where borough name was Manhattan then the Manhattan weather was combined. Similarly for the other boroughs, now the resulting dataframes were concatenated into one dataframe and the index was resetted. 

### Transformation 3
**Description:** Checking for Null Values
**Soundness Justification:** 
[3] Checking null values 
Since weather data was only for June upon integrating data the chunk of data chosen had few records from month of May so their weather data was null and they were dropped.
Since every case call has a closing time and there were two null values in closing timestamp they had to be dropped since they reflect errors in reporting from the department. 
Arrival timestamp had multiple empty field which were filled with NaT as sometimes multiple dispatch units are intimated and some reach faster and the other units are called off. Dropping these columns would hinder with analysis. 

### Transformation 4
**Description:** Reducing Columns
**Soundness Justification:**
[4] Column Incident date and Incident time were combined to create Incident timestamp column 
There was no snowfall in the month of June so snowfall and snowfall depth were dropped as well 
Now that time of weather was split into date and hour which can help in further analysis , the time column was dropped as well. 

### Transformation 5
**Description:** Introducing new columns
**Soundness Justification:**
[5] Description was split into Reason Category and Reason to help in analysis with respect to the category of crime/incident. Resulting in dropping description column.
To calculate how long the dispatch unit took to arrive on scene Time Taken column was created by finding time difference between Dispatch Time and Arrival Time. 
Using Time Taken column which was in timedelta format I converted it into time in minutes for analysis and Time taken was dropped.

## Visualizations
### Visual -  BoroHist.png
**Analysis:**
This is a histogram showing us frequency of 911 calls from each borough. It telss us that the most number of calls have been recieved in Brooklyn and least at Staten Island, this is indicative of two factors, Crime Rate and Area, area not so much though. It indicates the there is high crime reporting in Brooklyn and that the crime reporting is less in Staten Island, but again it is possible that Staten Island is very small in size and hence crime is less which in turn results in less reporting of crimes.

### Visual -  PatrolBoroHist.png
**Analysis:**
This is a histogram showing the frequency of call taken by which specific NYPD patrol in that particular borough. This chart indicates that Staten Island has recieved the least calls and Bronx NYPD patrol have recieved the highest. Note :- Bronx and Staten Island Patrol units dont have North and South division.

### Visual -  PrecinctHist.png
**Analysis:**
This is a histogram showing how many calls have been recieved by NYPD in the jurisdiction of a certain precinct. The chart indicates that the 14th Precinct has recieved the most number of calls in the said period of time and the 22nd Precinct has recieved the least calls. From this we can make a slight inference that precinct number 14 can be of Brooklyn borough and precinct number 22 can be of Staten Island.

### Visual -  ReasonHist.png
**Analysis:**
This is a histogram showing which category was the reported crime/issue from the complainant in the call. This graph is not very helpful as their are multiple categories that are reported very rarely in comparison with OTHER. This might be due to many reported crimes not being very specific from the caller and could not be classified appropriately. Second to the Other category would be calls to INVESTIGATE POSSIBLE CRIME.

### Visual -  ScatterForLatitude.png
**Analysis:**
This is a scatter plot amongst the quantitave data in our dataset. The first plot is between latitude and logitutde and when we think about it when superimposed on the map of New York it will give us a vague picture of where most of the calls are coming from. This plot serves slightly as a map of NY state. 

The second plot is latitude vs temperature in said latitude. Again not much can be inferred from this plot. the scatter plot is very uniform indicating the variable weather in respective latitudes in the month of June

The third plot is a latitude vs time taken to arrive on scene in minutes scatter plot. This indicates that regions within 40.5 and 40.6 latitude have far lesser response times than the others. 

The fourth plot is latitude vs rain in millimetres. This again is very generic and doesnt directly give any inference with respect to response times. Between latitude 40.7 and 40.9 there has been more rain in the month of June than any other area of NY state. But the most rainfall was seen in areas between 40.5 and 40.7 latitude. (In the month of June 2024)

### Visual -  ScatterForTemp.png
**Analysis:**
This is a scatter plot amongst the quantitave data in our dataset. In this the first plot is temperature of the region vs the rainfaill in millimetres. We can see that when the temperature is between 18 C and 30 C there has been cases of rainfall. This scatter plot doesnt provide much information for response time analysis.

The second plot is a temperature in C vs time taken to arrive on scene in minutes scatter plot. This tells us that when the temperature is on the both extreme ends that is in and around 15 C and 35 C the response time has been less comparitively. 

### Visual -  ScatterForLong.png
**Analysis:**
This is a scatter plot amongst the quantitave data in our dataset.The first plot is longitude vs temperature in the region. This doesnt give us much insight in analysis of response times. But we can infer that region between -73.8 and -73.7 longitude does not usually experience temperature above 30C and region between -74.05 and -74.25 dont usually experience whether below -15 degrees.(All in the month of June)

The second plot is logitutde vs rainfall in millimetres. Given the density of the plot we can infer that regions between -74.25 and -74.05 longitude experience less rains compared to the other regions of New York City. This directly doesnt help in analysis of response times but in connjunction with another scatter plot can help us.

### Visual -  ScatterForTime.png
**Analysis:**
This is a scatter plot amongst the quantitave data in our dataset. In this we see a scatter plot of time taken to arrive at scene in minutes vs Rain in millimetres. We can infer that irrespective of the rain the dispatch units have reached quickly. It is interesting to see that dispatch units have taken hours together to arrive at scene at times even when there was no rain and in cases with heavy rain they have still managed to reach faster. 

In the second plot we see that regions lying between longitude of -74.05 and -74.25 have faster response time than those in the region with longitude -73.7 to -74.05. One more inference is the region at and around -74.05 has had dispatch units arrive in little to no time.
