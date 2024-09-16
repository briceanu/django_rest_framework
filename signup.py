import requests

#     path('admin/', admin.site.urls),
#     path('create_truck',create_truck,name="create_truck"),
#     path('signup',signup,name='signup'),
#     path('login',login,name='login'),
#     path('save_working_day',save_working_day,name='save_working_day')
#  ]





url = 'http://localhost:8000/signup'
 

# body={"username":"teodorbriceanu","password":""}
 
body2 = {
    "username": "gigi",
    "password": "gigi123AF",  # Use correct password format
    "confirm_password": "gigi123AF",
    "email": "gigi@gmail.com"
}

# johnluis   password == gigi123A
# marian == gigi123AC
# gigi == gigi123AF

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI2MTQzMDU4LCJpYXQiOjE3MjYxMzk0NTgsImp0aSI6IjA0ZGM4MDkyN2MzZDRhZTdiZjg0ZGIwMGM3YWQ1ZDU1IiwidXNlcm5hbWUiOiJ0ZW9kb3JicmljZWFudSJ9.GhSeD8hOCnOKPUXKA6t4v7b2RmuR90NPgBve9wTh0rw"
}
# request = requests.post(url=url,data=body)
request = requests.post(url=url,data=body2)


print(request.text, request.status_code)