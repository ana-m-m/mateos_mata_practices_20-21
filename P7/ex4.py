import http.client
import json
import Seq1

def print_colored(message, color):
    from termcolor import colored, colored
    print(colored(message, color))
DICT_GENES = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000228296",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078 ",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362 "
}

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/"
ID = DICT_GENES["MIR633"]
PARAMETERS = "?content-type=application/json"

connection = http.client.HTTPConnection(SERVER)


try:
    user_gene = input("Enter the Gene that you want to analyse: ")
    id = DICT_GENES[user_gene]
    connection.request("GET", ENDPOINT + ID + PARAMETERS)
    response = connection.getresponse()
    if response.status == 200:
        response_dict = json.loads(response.read().decode())
        # print(json.dumps(response_dict, indent=4, sort_keys=True))
        sequence = Seq1.Seq(response_dict["seq"])
        print("Gene: ", user_gene)
        description = response_dict["desc"]
        print("Description:", description)
        s_length = sequence.len()
        print(" Length:", s_length)

        percentages = sequence.base_percentage()
        print(percentages)

        most_frequent_base = sequence.frequent_base(percentages)

        print("most frequent base: ", most_frequent_base)
except KeyError:
    print("the gene is not inside our dictionary, choose on eof the following:", list(DICT_GENES.keys()))
