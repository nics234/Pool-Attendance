import pandas as pd
import numpy as np 
import datetime as dt
import config 

path = config.path

pool_data = pd.read_csv(path, sep =";")

class DataTransformer()
  def __init__(self, pool_data):
    self.pool_data = pool_data
  
  def typetransformer(self):
    for _ in self.pool_data.Date:
      try:
        dt.datetime.strptime(_, "%m/%d/%y")
       except ValueError:
        dt.datetime.strptime(_, "%m.%d.%y")
        
    return pool_data

  def weekdaygetter(self):
    
    
    
  def Holidaygetter(self):
    
  class HistoricWeather()
    
  def get_lat_lon(self):
    address = "Brooklyn Betsy Head park"
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
    response = requests.get(url).json()
    lat = response[0]["lat"]
    lon = response[0]["lon"]
    
  def get_weather info
  API = https://open-meteo.com/en/docs/historical-weather-api
  
    
    
  class Poolforecast
  
    def get_closest_three_locations
    "https://stackoverflow.com/questions/41336756/find-the-closest-latitude-and-longitude"
    
    def get_weather_forecast_for closest three locations
    
    
    def predict attendance for each of the three locations 
    
    def display occupancy rate to give recommendation which pool to visit. 
    
    
    
    
  
  
    
    
