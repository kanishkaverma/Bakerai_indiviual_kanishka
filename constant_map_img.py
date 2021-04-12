import requests
import constants
 
base_url = "https://maps.googleapis.com/maps/api/staticmap?"
focus = "london"
zoom_level = 10

formats = 'text'

r = requests.get(base_url + "center=" + focus + "&zoom=" +
                   str(zoom_level) + "&size=400x400&key=" +
                             constants.API_KEY_STATIC_MAPS)
#  headers={
#    "X-RapidAPI-Host": "alexnormand-dino-ipsum.p.rapidapi.com",
#    "X-RapidAPI-Key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
#  }
f = open('./test.png', 'wb')
f.write(r.content)

f.close()
 