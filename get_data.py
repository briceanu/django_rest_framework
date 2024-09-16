import requests






get_data = 'http://localhost:8000/get_data?registration_plate=GL-138-YEB&km=1000'
get_km = 'http://localhost:8000/get_km?registration_plate=GL-138-YEB&username=johnluis'
increase_km = 'http://localhost:8000/increase_km?registration_plate=GL-138-YEB&km=2000'
 
 
request = requests.get(url=increase_km)


print(request.text, request.status_code)