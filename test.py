# import requests

# BASE_URL = "http://api.openweathermap.org/data/2.5/weather?lat="
# API_KEY = "77870069d2447b79ae6c8f9cc771849b"

# lat, lon = (29.881788, 81.523720)

# url = BASE_URL + str(lat) + "&lon=" + str(lon) + "&appid=" + API_KEY

# response = requests.get(url).json()

# print(response)

def loadingBar(percentage):
    percentage = percentage * 100
    if percentage == 0: return "[                    ]"
    elif percentage == 100: return "[====================]"
    else: return "[" + "="*int(percentage/5) + " "*(20-int(percentage/5)) + "]"

from datetime import datetime

no = 1
i = 122
j = 132
lat = 21.2
lon = round(71.344444349, 1)
api_key = "1aa4ac0bf96751229e6502b8d296a808"

now = datetime.now()
print(now.strftime("%d%m%Y-%H%M%S-%f"), api_key, loadingBar((119*359)/(120*360)), '%2d  %3d-%-3d %3.2f-%-f'%(no, i, j, lat, lon))

print(int((52)/(69)*420))