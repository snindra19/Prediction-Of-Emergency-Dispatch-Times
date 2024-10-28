## Revised Project Proposal
#### Analysis of 911 Calls
##### (10/28/2024)

Keywords: Dispatch Response times, Machine Learning, Weather

Description: The projects aim is to analyse 911 calls recieved by the NYPD and deduce insights about the nature of the call and analysis of incidents in the borough. We aim to answer questions what type of crime 
is more likely to happen in which borough of NYC and if there is any relationship between response time and the other features and if that would help predict the nature of the crime.
The inferences to be made using the following questions:-
* Data that is being analyzed is Dispatch Times and Weather Data.
* Which feature is more interlinked to response time ?
* Does the model perform better for any other first responders?
* What specific areas take the longest time ?

Research Questions
RO1:- To describe the trends within the boroughs of NYC to visualise crime statistics
RO1:- To describe the trends within Catgeory of crime on how what incident is reported more
RO1:- To describe trends within Latitude and other quantitative features to see if there are more incidents reported in that specific latitude with respect to the longitude, temperature, rainfall and response time.
RO1:- To describe trends within Longitude and other quantitative features to see if there are more incidents reported in that specific Longitude with respect to the temperature and rainfall.
RO1:- To describe trends within temperature and other quantitative features to see if there are more incidents reported in that specific temperature with respect to the temperature and response time.

RO2:- (Regression) To predict time taken by the NYPD to reach the scene based on factors like latitude, longitude and weather

RO3:- To defend the model for predicting the time taken by dispatch to arrive on scene in RO2 by evaluating different metrics and validating the model.

RO4:- To evaluate the causal relationships implied by the RO2 model

Intellectual Merit:
This project will help us uncover the factors that influence dispatch response times and to see if weather and incident reported have any connection. We can identfy what are the hotspot of crime in the given city. 
We can gain information like what time of the day do more crimes happen and with all this information the police can optimise or change their strategies and alter the allocation of their resources like manpower and 
patrol units.

Data Sourcing: 

The government website databases provide statistics on response times in past incidents. For the US government from Data.gov. This source provides real time and historical data on emergency dispatch incidents.
For weather data we can use Open Meteo which provides historical data on weather conditions. 
Cities like New York and Chicago have their own data put up on public portals as well
For retrieving real time data we can use RESTful APIs or use web scraping tools beautifulSoup or scrapy

 
Background Knowledge:

Emergency Response Systems and Operations
Source: Aringhieri, R., Bruni, M. E., Khodaparasti, S., & van Essen, J. T. (2017). Emergency medical services and beyond: Addressing new challenges through a wide literature review. 
Computers & Operations Research, 78, 349-368.
It is essential to understand how emergency response system work including their operations, techniques and challenges. it will help in understand the key performance indicators in emergency response and what are the traditional approaches in EMS. The challenges which they address might be solved with this project. 

Deep Learning Techniques for Time Series Prediction and Optimization
Source: Lim, B., & Zohren, S. (2021). Time-series forecasting with deep learning: a survey. Philosophical Transactions of the Royal Society A, 379(2194), 20200209.
This survey provides an overview of deep learning techniques applied to time series data which is necessary for predicting optimised emergency routes and reduced response time. It covers various architectures like RNN, LSTM and CNN and handles multivariate data.

Spatial Data Analysis and Geographic Information Systems (GIS) in Emergency Management
Source: Stevensonp, M., & Hendrikx, J. (2019). Spatial and Temporal Analysis in the Context of Emergency Management. In A. Farazmand (Ed.), Global Encyclopedia of Public Administration, Public Policy, and Governance (pp. 1-7). Springer International Publishing.
This chapter provides insights on the use of spatial data analysis in emergency management. It helps in understanding spatial and temporal analysis in emergency response, integration of different data sources for spatial analysis. Spatial analysis is very crucial give that it helps in better resource allocation based on geographical factors.

These three sources provide a strong foundation in the projects domain :-
* Emergency response systems
* Techniques applicable to time series prediction and optimization
* Spatial data analysis for emergency management



Related Work: 
 * [1] A Review of Emergency Incident Prediction, Resource Allocation, and Dispatch Models by Ayan Mukhopadhyay , Geoffrey Pettet , Sayyed Vazirizade ,
 Yevgeniy Vorobeychik , Mykel Kochenderfer , Abhishek Dubey
 * [2] Spatiotemporal Data-Driven Multiperiod Relocation Optimization of Emergency Medical Services by by Xinxin Zhou, Yujie Chen, Yingying Li, Bingjie Liu and Zhaoyuan Yu
 *  [3] 911 Analysis: Call Data Shows We Can Rely Less on Police 
https://vera-institute.files.svdcdn.com/production/downloads/publications/911-analysis-we-can-rely-less-on-police.pdf
* [4] Re-assessing measurement error in police calls for service: Classifications of events by dispatchers and officers by Rylan Simpson, Carlena Orosco
* [5] Big Data Analysis Examining	the	Meaning	of	Boston’s 911 Call Data and Implications for	Public	Policy by Dr. Jack McDevitt, Keller Sheppard, and Stephen Douglas
* [6] Analysis and Prediction of 911 Calls based on Location using Spark Big Data Platform by Ketki Deshpande, Shruti Pandey, Sukhada Deshpande
* https://hpcf-files.umbc.edu/research/papers/IS789_Project_Report-HPCF-2019-29.pdf
