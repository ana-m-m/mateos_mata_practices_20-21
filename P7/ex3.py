import http.client
import json
DICT_GENES = {
    "FRAT1" : "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "RNU6_269P" : "ENSG00000212379",
    "MIR633" : "ENSG00000207552",
    "TTTY4C" : "ENSG00000228296",
    "RBMY2YP" : "ENSG00000227633",
    "FGFR3" : "ENSG00000068078 ",
    "KDR" : "ENSG00000128052",
    "ANK2" : "ENSG00000145362 "
}

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/"
ID = DICT_GENES["MIR633"]
PARAMETERS = "?content-type=application/json"

connection = http.client.HTTPConnection(SERVER)
connection.request("GET", ENDPOINT+ID+PARAMETERS)
response = connection.getresponse()
print("response received : ", response.status, response.reason)

# control server error
if response.status == 200:  # controlar la disponibilidad del servidor

    response = json.loads(response.read().decode())

    # from dictionary to string, also formated|
    # print(json.dumps(response, indent=4, sort_keys=True))

    print("Gene:", ID)
    print("Description:", response["desc"])
    print("Bases: ", response["seq"])
elif response.status == 484:
    print("check if the ENDPOINT was well writen")
