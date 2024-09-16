import requests




url = 'http://localhost:8000/login'


body={"username":"gigi","password":"gigi123AF"}
# url2 = 'http://localhost:8000/signup'


# johnluis   password == gigi123A
# marian == gigi123AC
# gigi == gigi123AF



request = requests.post(url=url,data=body)


print(request.text, request.status_code)