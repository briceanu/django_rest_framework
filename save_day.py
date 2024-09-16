import requests


url = 'http://localhost:8000/save_working_day'
 

# body={"username":"teodorbriceanu","password":""}
 
body2 = {
    "username": "gigi",
    "start_time": "2020-07-28T5:40:40",
    "end_time": "2020-07-28T15:16:40",
    "load_carried": 54,
    "fuel_consumption":642,
    "km_driven":669,
    "truck_used":"GL-138-YEB" 
}

# john_luis == gigi123A
# john_luis  == gigi123A
# marian == gigi123AC
# gigiel == gigi123AF


headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI2NDA5MzQ3LCJpYXQiOjE3MjY0MDU3NDcsImp0aSI6IjVlNmViOTE1MmY5MDQyZTY5MjFlNmE5MjIzNTRjODZkIiwidXNlcm5hbWUiOiJnaWdpIn0.kjA-dzN2dBR9GO0Rj_W9KGpCa0cbxIEyXxc8nEh35Nc"
}
# request = requests.post(url=url,data=body)
request = requests.post(url=url,data=body2,headers=headers)


print(request.text, request.status_code)