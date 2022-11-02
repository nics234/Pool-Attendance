# Pool-Attendance project
This repository contains all the steps undertaken to build and establsh the pool attendance forecasting. 


# User story
The user can go the webpage and from a drop-down menu selection the public pool in NYC he or she wants to attend. 
Based on the selection of the location a weather-forecast will be generated and then based on historic data the tool will put out and estimation of how many visitors the pool might see on the next couple of days. 

# Data sources
NYC Pool Attendance data is derived from: 
Historical weater data is derived from: 
Weather forecast data is derived from: 
US Holiday data is derived from:



# Approach 
1. Enrich Data\n
  a. Get weekday
  b. Get information about holidays in the U.S.\n
  c. Get latitude and longtitude of the pool location\n
  d. Get weather on said date --> based on the region
  e. Get information about maximum pool capacity
  
 2. Build prediction model 
  a. Extract relevant information 
  b. Build regression NN to predict attendance for specific day 
  
 3. By location of a person
  a. get 3 closest pools 
  b. get respective attendance and attendance percentage 
  
