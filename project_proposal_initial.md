#### Predictive Emergency Dispatch Systems Using Python and Machine Learning
##### Sai Ganesh
##### (09/11/2024)

Keywords: Predictive Dispatch Response times, Traffic, Weather

Description: The projects main aim is to find a reduced first responders dispatch time with the help of traffic, weather and geospatial data. This does not use any integration of external frameworks like flask or any web deployment platforms. It comprises of development of a predictive model to reduce response times using a data driven approach by leveraging pythons machine learning libraries like PyTorch or TensorFLow and integrate real time data into predictions
The inferences to be made using the following questions:-
* Data that is being analyzed is Dispatch Times, Traffic Data and Weather Data.
* Which feature effects response time predictions more, traffic or weather?
*  Does the model perform better for any other first responders?
* What specific areas take the longest time and how can the model improve the time?


Intellectual Merit:

This project uses machine learning to predict emergency vehicle response based on real-time data. It is an innovative application of neural networks which will offer us insights on how AI can optimize such critical decisions. This area of research can have broader implications for any other time bound event as well.
The approach of catering to multiple features like dispatch time, weather and road conditions can yield new findings on other important features influenced by response times. This can help emergency services to react better and faster.


Data Sourcing: 

The government website databases provide statistics on response times in past incidents. For the US government from Data.gov. This source provides real time and historical data on emergency dispatch incidents.
Public traffic and geospatial API's like google maps API for real time and historical data on traffic.
For weather data we can use OpenWeatherMap which provides historical data on weather conditions. 
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
This chapter provides insights on the use of spatial data analysis in emergency management. It helps in understanding spatial and temporal analysis in emergency response, integration of different data sources for spatial analysis. Spatial analysis is very crucial give that it helps in better resource allocation and route optimisation based on geographical factors.

These three sources provide a strong foundation in the projects domain :-
* Emergency response systems
* Deep learning techniques applicable to time series prediction and optimization
* Spatial data analysis for emergency management



Related Work: 
 * [1] A Review of Emergency Incident Prediction, Resource Allocation, and Dispatch Models by Ayan Mukhopadhyay , Geoffrey Pettet , Sayyed Vazirizade ,
 Yevgeniy Vorobeychik , Mykel Kochenderfer , Abhishek Dubey
 * [2] Spatiotemporal Data-Driven Multiperiod Relocation Optimization of Emergency Medical Services by by Xinxin Zhou, Yujie Chen, Yingying Li, Bingjie Liu and Zhaoyuan Yu