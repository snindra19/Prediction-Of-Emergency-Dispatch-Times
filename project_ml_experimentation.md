#### Experimentation
#### (Analysis of 911 Calls)
#### (Sai Ganesh Nindra)
#### (11/25/2024)


## Explainable Records
### Record 1
**Raw Data:** 'CAD_EVNT_ID':103529625,'CREATE_DATE':'5/31/2024','INCDENT_TMSTMP':'5/31/2024 22:27','NYPD_PCT_CD':70,'BORO_NM':'BROOKLYN','PATRL_BORO_NM':'PATROL BORO BKLYN SOUTH','GEO_CD_X':997339,'GEO_CD_Y':164281,'RADIO_CODE':'10P2','REAS_CTGRY':'INVESTIGATE/POSSIBLE CRIME','REASON':'SUSP PERSON/OUTSIDE (PROWLER)','CIP_JOBS':'Non CIP','ADD_TS':'5/31/2024 22:27','DISP_TS':'6/1/2024 0:21','ARRIVD_TS':'6/1/2024 3:09','TIM_MIN':168,	'CLOSNG_TS':'6/1/2024 3:12','Latitude':40.617588,'Longitude':-73.952855,'date':'6/1/2024','hour':0,'temperature_2m (°C)':16.2,	'precipitation (mm)':0,	'rain (mm)':0

Prediction Explanation:** For this input the predicted value was 3.02 minutes. This is in my opinion a good prediction. Given that brooklyn's land area is just 71 square miles of land of which road netwrok would be lesser and Brooklyn South would be even more smaller. There are 13 precincts under south brooklyn division which is the most among the sectors of New York. Given NYPD's large network and fleet 3.02 minutes to reach a scene is commendable and a desired time. Borough, the patrol unit sector and the Precinct number all indicate it is in the vicinity of south brooklyn. If time taken in the real world scenario is much larger then it might be due to other factors relating to the situation at hand which has many possible cases or a human error. Hence I feel 3.02 is a good and must achieve time.

### Record 2
**Raw Data:** 'CAD_EVNT_ID':103531241,'CREATE_DATE':'5/31/2024','INCDENT_TMSTMP':'5/31/2024 23:40','NYPD_PCT_CD':115,
    'BORO_NM':'QUEENS','PATRL_BORO_NM':'PATROL BORO QUEENS NORTH','GEO_CD_X':1020196,'GEO_CD_Y':214821,  'RADIO_CODE':'52K6','REAS_CTGRY':'DISPUTE','REASON':'KNIFE/FAMILY','CIP_JOBS':'Non CIP','ADD_TS':'5/31/2024 23:40','DISP_TS':'6/1/2024 0:31','ARRIVD_TS':'6/1/2024 0:33','TIM_MIN':1.85,'CLOSNG_TS':'6/1/2024 0:38','Latitude':40.756246,'Longitude':-73.870254,'date':'6/1/2024','hour':0,'temperature_2m (°C)':16.3,'precipitation (mm)':0,
    'rain (mm)':0

Prediction Explanation:** For this input the predicted value is 3.62 which is basically asking for some improvement in the NYPD's already quick response time. This prediction is exemplary as the recorded time on this was 3.62 minutes. Queens is relatively larger than Brooklyn but again given Jamaica and Rockaway's increase in crime rates, the NYPd should increase patrol services and respond as quick as possible even if it is below their current 1.85 minutes in said case. 

## Interesting Features
### Feature A
**Feature:** NYPD_PCT_CD

**Justification:** Given that the precinct number that takes up the case needs to be close to the complainant so as to 
respond as quick as possible. We cannot have a precinct that is in another borough respond to a call which is not from the same borough as that precinct is in as it will just delay the process of arrive on the scene. And it is common knowledge that a precinct after all has a location, which in our data's sense are coordinates corresponding to its latitude and longitude, a precinct is a part of a region in the city of New York corresponds to the borough name feature as well. So in my opinion yes the precinct number is an interesting feature that might have significant impact on the predicition. 

### Feature B
**Feature:** rain (mm)

**Justification:** Though the model doesnt understand the real world effects of adverse temperature on travel, the model should have caught on to trends where adverse temperatures, spike or dip in the centigrade would affect the time taken by the dispatch units to reach the scene. We know that with very low or very high temperatures there are a lot of medical emergencies, people rushing home or falling sick and there is a lot of traffic on the road. With adverse conditions like heavy rainfall, snow or fog, temperature goes very low and this affects travel as well. So this will impact the model in predicting the time taken to reach on scene.

## Experiments 
### Varying A
**Prediction Trend Seen:** Varying A i.e the precinct number it can be seen that though the model doesnt know the actual locations of each borough it has almost captured the trend where the further the borough the longer it takes to reach, for raw input 1 the location is in south brooklyn and the output produced on varying the precinct number with respect to different borough was as follows, Manhattan South the least, Staten Island second least, Brox and Queen much higher. In the real world as well, this loosely follows. 

### Varying B
**Prediction Trend Seen:** Varying B i.e the amount of rainfall in millimetres it can be seen that there is an increase in the time when we increase the rainfall level. The more the rainfall the time increases with a small increment. The model however didnt capture anything at an extreme since the dataset used is of the month July and there hasnt been any storms or heavy rainfall and hence failed to catch high and abnormal values. The max it increased was by 25%.

### Varying A and B together
**Prediction Trend Seen:** For together I would like to propose a relation like further precint higher rainfall and closer precint lower rainfall. For a closer precinct and lower rainfall the output is a slightly lower time whereas when the precinct is far and the rainfall is very high the time taken also increased drastically by almost 40%. While varying values together the outputs are opposite when both are on the lower end the time also reduces and when both are on the higher end the time taken also increases.

### Varying A and B inversely
**Prediction Trend Seen:** For inversely i would like to propose a relation like further precinct less rainfall and closer precinct higher rainfall. And the trend that emerged here is such that the time increased but not by much, whereas if the precinct is closer and there is high rainfall too the time didnt increase by much. When capturing trends by inversely changing values the outcome always is higher but not by much. 