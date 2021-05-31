import http.client
import json


# definition to get the information, rest api
def httpget(server, port, request):
    connection = http.client.HTTPConnection(server, port)
    print(f"\nConnecting to server: {server}:{port}\n")
    try:
        connection.request("GET", request)
    except ConnectionRefusedError:
        print(f"ERROR! Cannot connect to the Server: {server}\n"
              f"    request: {request}")
        exit()
    response = connection.getresponse()
    print(f"Response received of request: {request}\n"
          f"    Status, Reason: {response.status} {response.reason}\n")
    data = response.read().decode("utf-8").replace("'", '"')
    output = json.loads(data)
    return output


PORT = 8080
SERVER = 'localhost'

requests = ["/listSpecies?limit=2&json=1", "/karyotype?specie=mouse&json=1",
            "/chromosomeLength?specie=mouse&chromo=12&json=1", "/geneSeq?gene=FRAT1&json=1",
            "/geneInfo?gene=FXN&json=1", "/geneCalc?gene=RNU6_269P&json=1"]

information = {}
for req in requests:
    info = httpget(SERVER, PORT, req)

    # print in the console the information
    print("INFORMATION:")
    for key, value in info.items():
        print(f"    {key}: {value}")

    # information dictionary will store all the data related with its request:
    information[req] = info
