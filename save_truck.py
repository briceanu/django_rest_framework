import requests

#     path('admin/', admin.site.urls),
#     path('create_truck',create_truck,name="create_truck"),
#     path('signup',signup,name='signup'),
#     path('login',login,name='login'),
#     path('save_working_day',save_working_day,name='save_working_day')
#  ]





url = 'http://localhost:8000/create_truck'
 

# body={"username":"teodorbriceanu","password":""}
 
body2 = {
    "brand": "Mercedes Actros",
    "year_of_build": "2021-10-22",  # Use correct date format
    "fuel_type": "diesel",
    "registration_plate": "B-378-LEB"
}

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI2MzI4ODI0LCJpYXQiOjE3MjYzMjUyMjQsImp0aSI6IjIzZGU3MTU4NDc0ODQwMGZhODVmNjNlMGJhNmFkZmMyIiwidXNlcm5hbWUiOiJ0ZW9kb3JicmljZWFudSJ9.dRiapWKQSmmsl74A2QId3_IhI9teOJVfG9UOD_A9XJE"
}
# request = requests.post(url=url,data=body)
request = requests.post(url=url,data=body2,headers=headers)


print(request.text, request.status_code)