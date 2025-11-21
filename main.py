import requests
from datetime import datetime
MY_LAT = 49.023880
MY_LNG = -122.801178



# # response = requests.get("https://api.wheretheiss.at/v1/satellites/25544")
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()
# # ["iss_position"]["longitude"]["latitude"]
# # if response.status_code == 404:
# #     raise Exception("That resource does not exist.")
# # elif response.status_code == 401:
# #     raise Exception("You are not authorised to access this data")
# # print("Status code:", response.status_code)
# # print(response.json())
# print(data)
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunrise)

time_now = datetime.now()

print(time_now.hour)



