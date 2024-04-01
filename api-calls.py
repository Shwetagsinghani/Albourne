import requests
import json

data = {'id': 1,
        'name': 'xyz',
        'score': 5.2,
        'address': 'new'}

postRespose = requests.post("https://us-central1-testomate-test.cloudfunctions.net/api/restaurant", data=data )
print(postRespose.status_code)

if postRespose.status_code == 201:
    print("New Entry Created successfully")

data1 = {'id': 2,
        'name': 'xyz2',
        'score': 5.2,
        'address': 'new1'}

postRespose1 = requests.post("https://us-central1-testomate-test.cloudfunctions.net/api/restaurant", data=data1 )
print(postRespose1.status_code)

if postRespose1.status_code == 201:
    print("New Entry Created successfully")

patchResponse = requests.patch("https://us-central1-testomate-test.cloudfunctions.net/api/restaurant/1", data={'name' :'newName'})
print(patchResponse.status_code)

if patchResponse.status_code == 200:
    print("Resturant Name Updated From xyz to NewName Correctly")

deleteResponse = requests.delete("https://us-central1-testomate-test.cloudfunctions.net/api/restaurant/2")
print(deleteResponse.status_code)

if deleteResponse.status_code == 200:
    print("Resturant id 2 deleted success fully")

response = requests.get("https://us-central1-testomate-test.cloudfunctions.net/api/restaurants") 
print(response.json())
print(response.status_code)



