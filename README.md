# World_Weather_Analysis
We are working with Jack to develope a PlanMyTrip app. The testing version of the app works great. After the Beta version testing periods, we received several feedbacks for improving. These sugesstion includes : 

      *Travelers input statements to filter the data for their weather preferences, which will be used to identify potential travel destinations and nearby hotels.
      *From the list of potential travel destinations, travelers will choose cities to create a travel itinerary.
      *Finally, travelers will create a travel route between the four cities as well as a marker layer map.
      
## Travelers input statements to filter the data for their weather preferences :
We createed a random city location list over 2000 cities which included their weather information as shown below

https://github.com/ttan0408/World_Weather_Analysis/blob/main/Weather_Database_Summary.PNG

Then using these 2000 cities list, we add the temperature filter so that traveler can filter the preference temperature cities that they like to visit. The list after filtered is only shown the citi location where the max temperature is in the traveler input ranges, for example this list is showing cities which have temp between 75 F to 90 F :

https://github.com/ttan0408/World_Weather_Analysis/blob/main/Weather_Database_Summary_Temp_Filtering.PNG

The impproved app also use the Google map to show the cities and their information such as weather description

https://github.com/ttan0408/World_Weather_Analysis/blob/main/Vacation_Search/WeatherPy_vacation_map.png

## Travel Itinerary Map Creation :

We also enhance the app so that travelers can select cities and create their itineraries. The example map where the 4 city destinations is shown below :

https://github.com/ttan0408/World_Weather_Analysis/blob/main/Vacation_Itinerary/WeatherPy_travel_map.PNG

Within these four cities, travel can also look at layer maker map so they can understand how the current weather description look like :

https://github.com/ttan0408/World_Weather_Analysis/blob/main/Vacation_Itinerary/WeatherPy_travel_map_markers.png

The entire project files can be found at :

https://github.com/ttan0408/World_Weather_Analysis/tree/main/Weather_Database









