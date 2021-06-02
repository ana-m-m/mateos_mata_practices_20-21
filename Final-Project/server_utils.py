from pathlib import Path
import pathlib
import colorama
import requests
import termcolor
from jinja2 import Template


# CLASS SEQ
class Seq:
    NULL_SEQUENCE = "NULL"
    INVALID_SEQUENCE = "ERROR"

    def __init__(self, bases=NULL_SEQUENCE):
        self.strbases = bases
        if self.strbases == Seq.NULL_SEQUENCE:
            print("NULL Sequence created")
        else:
            if Seq.valid_sequence(self.strbases):
                print("New sequence is created")
            else:
                self.strbases = Seq.INVALID_SEQUENCE
                print("INVALID Seq!")

    def __str__(self):
        return self.strbases

    def len(self):
        if Seq.valid_sequence(self.strbases):
            return len(self.strbases)
        else:
            return 0

    def count_base(self, base):
        base_count = 0
        if Seq.valid_sequence(self.strbases):
            for i in self.strbases:
                if i == base:
                    base_count += 1
        return base_count

    def count(self):
        base_dict = {"A": 0, "C": 0, "T": 0, "G": 0}
        if Seq.valid_sequence(self.strbases):
            for i in self.strbases:
                base_dict[i] += 1
        return base_dict

    def base_percentage(self):
        base_count_dict = Seq.count(self)
        strbases_len = Seq.len(self)
        base_percent_list = []
        bases = []
        for base, count in base_count_dict.items():
            percent = (int(count) / strbases_len) * 100
            base_percent_list.append(round(percent, 1))
            bases.append(base)
        return dict(zip(bases, base_percent_list))

    def print_percentage(self, percentages):
        bases_count = list(Seq.count(self).values())
        bases_percent = list(percentages.values())
        bases = list(Seq.count(self).keys())
        msg = ""
        for i in range(len(bases)):
            msg += f"{bases[i]}: {bases_count[i]} ({bases_percent[i]}%)\n"
        return msg

    @staticmethod
    def frequent_base(dict_count):
        return max(dict_count, key=dict_count.get)

    def reverse(self):
        if Seq.valid_sequence(self.strbases):
            return self.strbases[::-1]
        else:
            return self.strbases

    def complement(self):
        if Seq.valid_sequence(self.strbases):
            comp_bases = {"A": "T", "T": "A", "C": "G", "G": "C"}
            comp_seq = ""
            for i in self.strbases:
                comp_seq += comp_bases[i]
            return comp_seq
        else:
            return self.strbases

    def read_fasta(self, filename):
        sequence = Path(filename).read_text()
        sequence = sequence[sequence.find("\n") + 1:].replace("\n", "")
        self.strbases = sequence

    @staticmethod
    def valid_sequence(bases):
        nucleic_bases = "ACGT"
        for base in bases:
            if base not in nucleic_bases:
                return False
        return True


# DICTIONARY WITH GENES FOR MEDIUM LEVEL
genes_dict = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000226906",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSMUSG00000062960",
    "ANK2": "ENSG00000145362"}


# OTHER USEFUL DEFINITIONS

def read_template_html_file(filename):
    content = Template(pathlib.Path(filename).read_text())
    return content


def print_colored(message, color):
    colorama.init()
    print(termcolor.colored(message, color))


# create a json file using context -> request.json
def create_request_json(context):
    json_content = str(context)
    json_name = "./request.json"
    json_file = open(json_name, "w+")
    json_file.write(json_content)
    json_file.close()
    return json_name


def read_json(json_name):
    contents = pathlib.Path(json_name).read_text()
    content_type = 'application/json'
    return contents, content_type


def read_html(path_name, context):
    contents = read_template_html_file(path_name).render(context=context)
    content_type = 'text/html'
    return contents, content_type


# create a dot list in html format using a list
def list_to_dot_html_list(list):
    dot_html_list = ""
    for i in range(len(list)):
        dot_html_list += "<li>" + str(list[i]).replace("_", " ") + "</li>"
    return dot_html_list


def dict_to_list(dict):
    list = []
    for key, value in dict.items():
        list.append(str(key) + " : " + str(value))
    return list


# return json or html depending of parameters
def json_or_html_return(arguments, context_html, context_json, html):
    if arguments.__contains__('json'):

        if arguments["json"][0] == str(1):
            print("json requested")
            request_json = create_request_json(context_json)
            contents, content_type = read_json(request_json)
            error_code = 200
            return contents, content_type, error_code
        else:
            contents, content_type = read_html("./html/Error.html", "The parameter to get json must be 1.")
            error_code = 404
            return contents, content_type, error_code

    else:
        contents, content_type = read_html(html, context_html)
        error_code = 200
        return contents, content_type, error_code


# DEFINITIONS FOR THE ENDPOINTS

def listSpecies(server, ext, arguments, html):
    try:
        r = requests.get(server + ext, headers={"Content-Type": "application/json"})

        dict_species = r.json()["species"]

        if not arguments.__contains__("limit"):
            # limit not specified -> list with all the species
            species = []
            for i in range(0, len(dict_species)):
                species.append(dict_species[i]["name"])
            species_html = list_to_dot_html_list(species)
            context_html = {"tot_species": len(dict_species), "limit": "NONE", "species": species_html}
            context_json = {"tot_species": len(dict_species), "limit": "NONE", "species": species}
            contents, content_type, error_code = json_or_html_return(arguments, context_html,
                                                                     context_json, html)

        else:
            # n limit -> list with n species
            limit = arguments["limit"][0]
            species = []
            for i in range(0, int(limit)):
                species.append(dict_species[i]["name"])
            species_html = list_to_dot_html_list(species)
            context_html = {"tot_species": len(dict_species),
                            "limit": limit,
                            "species": species_html}
            context_json = {"tot_species": len(dict_species),
                            "limit": limit,
                            "species": species}
            # json_or_html_return -> depending of arguments contain json parameter
            contents, content_type, error_code = json_or_html_return(arguments, context_html,
                                                                     context_json, html)

    except ValueError:
        contents, content_type = read_html("./html/Error.html", "Have to enter correct integer in limit parameter")
        error_code = 404
    return contents, content_type, error_code


def karyotype(server, ext, arguments, html):
    try:
        specie = arguments["specie"][0]
        r = requests.get(server + ext + specie + "?", headers={"Content-Type": "application/json"})

        karyotype = r.json()["karyotype"]
        karyotype_html = list_to_dot_html_list(karyotype)
        # different format for html, and json
        context_html = {"karyotype": karyotype_html}
        context_json = {"karyotype": karyotype}
        contents, content_type, error_code = json_or_html_return(arguments, context_html, context_json, html)

    except KeyError as e:
        contents, content_type = read_html("./html/Error.html",
                                           "Have to enter correct value in the parameter: " + str(e))
        error_code = 404
    return contents, content_type, error_code


def chromosomeLength(server, ext, arguments, html):
    try:
        specie = arguments["specie"][0]
        chromo = arguments["chromo"][0]
        r = requests.get(server + ext + specie + "?", headers={"Content-Type": "application/json"})

        chromosomes = r.json()["top_level_region"]
        for chromosome in chromosomes:

            if chromosome["name"] == chromo:
                chromo_len = chromosome["length"]
                context = {"chromo_len": chromo_len}
                contents, content_type, error_code = json_or_html_return(arguments, context, context, html)

    except KeyError as e:

        contents, content_type = read_html("./html/Error.html",
                                           "Have to enter correct value in the parameter: " + str(e))
        error_code = 404
    return contents, content_type, error_code


def geneSeq(server, ext, arguments, html):
    try:
        gene = arguments["gene"][0]
        if gene in genes_dict:
            """ext = "/sequence/id/"
            html = "./html/sequence_gene.html"""
            id = genes_dict[gene]

            r = requests.get(server + ext + id + "?", headers={"Content-Type": "text/x-fasta"})
            seq = r.text
            sequence = seq[seq.index("\n"):]

            context_html = {"gene": gene, "sequence": sequence}
            context_json = {"gene": gene, "sequence": sequence.replace("\n", "")}

            contents, content_type, error_code = json_or_html_return(arguments, context_html,
                                                                     context_json, html)

        else:
            contents, content_type = read_html("./html/Error.html", "Gene not found in gene dict")
            error_code = 404
    except KeyError as e:

        contents, content_type = read_html("./html/Error.html",
                                           "Have to enter correct value in the parameter: " + str(e))
        error_code = 404
    return contents, content_type, error_code


def geneInfo(server_info, ext_info, arguments, html):
    try:
        gene = arguments["gene"][0]
        if gene in genes_dict:

            id = genes_dict[gene]

            r = requests.get(server_info + ext_info + id + "?", headers={"Content-Type": "application/json"})

            start = r.json()["start"]
            end = r.json()["end"]
            length = str(int(end) - int(start))
            name = r.json()["assembly_name"]

            context = {"gene": gene, "id": id, "start": start, "end": end, "length": length, "name": name}
            contents, content_type, error_code = json_or_html_return(arguments, context, context, html)

        else:
            contents, content_type = read_html("./html/Error.html", "Gene not found in gene dict")
            error_code = 404
    except KeyError as e:

        contents, content_type = read_html("./html/Error.html",
                                           "Have to enter correct value in the parameter: " + str(e))
        error_code = 404
    return contents, content_type, error_code


def geneCalc(server_info, ext_info, arguments, html):
    try:
        gene = arguments["gene"][0]
        if gene in genes_dict:
            id = genes_dict[gene]

            r = requests.get(server_info + ext_info + id + "?", headers={"Content-Type": "application/json"})

            start = r.json()["start"]
            end = r.json()["end"]
            length = str(int(end) - int(start))

            ext_seq = "/sequence/id/"

            sequence = requests.get(server_info + ext_seq + id + "?content-type=text/plain")

            base_perc = Seq(sequence.text).base_percentage()
            base_perc_list = dict_to_list(base_perc)
            base_perc_html = list_to_dot_html_list(base_perc_list)

            context_html = {"gene": gene, "length": length, "base_perc": base_perc_html}
            context_json = {"gene": gene, "length": length, "base_perc": base_perc}

            contents, content_type, error_code = json_or_html_return(arguments, context_html,
                                                                     context_json, html)

        else:
            contents, content_type = read_html("./html/Error.html", "Gene not found in gene dict")
            error_code = 404
    except KeyError as e:

        contents, content_type = read_html("./html/Error.html",
                                           "Have to enter correct value in the parameter: " + str(e))
        error_code = 404
    return contents, content_type, error_code
