import requests
from io import BytesIO

from PIL import Image
import requests
import webbrowser
import keys 

def get_constant_map_img( home_address, zoom_level ): 
    base_url = "https://maps.googleapis.com/maps/api/staticmap?"
    focus = "london"
    # home_address = '221B Baker Street, london'
    zoom_level = 10

    formats = 'text'
    # print(keys.API_KEY_STATIC_MAPS)
    # print(base_url + "center=" + home_address +"&markers=" + home_address + "&size=400x400&key=" +  keys.API_KEY_STATIC_MAPS)
    r = requests.get(base_url + "center=" + home_address +"&markers=" + home_address + "&size=400x400&key=" +
                                keys.API_KEY_STATIC_MAPS)
    #  "&zoom=" +                 str(zoom_level)
    # img = Image.open(BytesIO(r.content))
    # img.show()
    f = open('./test.png', 'wb')
    f.write(r.content)

    f.close()
    if home_address == "221B Baker Street, London": 
        webbrowser.open_new_tab('address.html')
        # webbrowser.open('test.png') 
    
    return base_url + "center=" + home_address +"&markers=" + home_address + "&size=400x400&key=" +                     keys.API_KEY_STATIC_MAPS    
# get_constant_map_img('india',10)
 