import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping"
PARAMS = "?content-type=application/json"

connection = http.client.HTTPConnection(SERVER)
connection.request("GET", ENDPOINT + PARAMS)
response = connection.getresponse()
answer_decoded = response.read().decode()

# this is a string because of the decode function
print(type(answer_decoded), answer_decoded)

# this is a dictionary because of json()
dict_response = json.loads(answer_decoded)
print(type(dict_response), dict_response)

if dict_response["ping"] == 1:
    print("ping ok, database is running")
else:
    print("database is down!")

