import http.server
import socketserver
from urllib.parse import urlparse, parse_qs
import server_utils as su
import requests


PORT = 8080
# Prevents error: port already in use
socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print("Resource requested: ", path_name)
        print("Parameters: ", arguments)
        server = "https://rest.ensembl.org"
        server_info = "https://grch37.rest.ensembl.org"

        if path_name == "/":
            contents, content_type = su.read_html("./html/form.html", "")
            error_code = 200
        elif path_name == "/listSpecies":
            ext = "/info/species?"
            html = "./html/list_of_species.html"
            try:
                r = requests.get(server + ext, headers={"Content-Type": "application/json"})

                dict_species = r.json()["species"]

                if not arguments.__contains__("limit"):
                    species = []
                    for i in range(0, len(dict_species)):
                        species.append(dict_species[i]["name"])
                    species_html = su.list_to_dot_html_list(species)
                    context_html = {"tot_species": len(dict_species), "limit": "NONE", "species": species_html}
                    context_json = {"tot_species": len(dict_species), "limit": "NONE", "species": species}
                    contents, content_type, error_code = su.json_or_html_return(arguments, context_html,
                                                                                context_json, html)

                else:
                    limit = arguments["limit"][0]
                    species = []
                    for i in range(0, int(limit)):
                        species.append(dict_species[i]["name"])
                    species_html = su.list_to_dot_html_list(species)
                    context_html = {"tot_species": len(dict_species),
                                    "limit": limit,
                                    "species": species_html}
                    context_json = {"tot_species": len(dict_species),
                                    "limit": limit,
                                    "species": species}
                    contents, content_type, error_code = su.json_or_html_return(arguments, context_html,
                                                                                context_json, html)

            except ValueError:
                contents, content_type = su.read_html("./html/Error.html", "Have to enter correct integer in limit parameter")
                error_code = 404

        elif path_name == "/karyotype":
            ext = "/info/assembly/"
            html = "./html/karyotype.html"
            try:
                specie = arguments["specie"][0]
                r = requests.get(server + ext + specie + "?", headers={"Content-Type": "application/json"})

                karyotype = r.json()["karyotype"]
                karyotype_html = su.list_to_dot_html_list(karyotype)

                context_html = {"karyotype": karyotype_html}
                context_json = {"karyotype": karyotype}
                contents, content_type, error_code = su.json_or_html_return(arguments, context_html, context_json, html)

            except KeyError as e:
                contents, content_type = su.read_html("./html/Error.html", "Have to enter correct value in the parameter: "+ str(e))
                error_code = 404
        elif path_name == "/chromosomeLength":

            ext = "/info/assembly/"
            html = "./html/len_chromo.html"
            try:
                specie = arguments["specie"][0]
                chromo = arguments["chromo"][0]
                r = requests.get(server + ext + specie + "?", headers={"Content-Type": "application/json"})

                chromosomes = r.json()["top_level_region"]
                for chromosome in chromosomes:

                    if chromosome["name"] == chromo:
                        chromo_len = chromosome["length"]
                        context = {"chromo_len": chromo_len}
                        contents, content_type, error_code = su.json_or_html_return(arguments, context, context, html)

            except KeyError as e:

                contents, content_type = su.read_html("./html/Error.html",
                                                      "Have to enter correct value in the parameter: " + str(e))
                error_code = 404

        elif path_name == "/geneSeq":

            try:
                gene = arguments["gene"][0]
                if gene in su.genes_dict:
                    ext = "/sequence/id/"
                    html = "./html/sequence_gene.html"
                    id = su.genes_dict[gene]

                    r = requests.get(server + ext + id + "?", headers={"Content-Type": "text/x-fasta"})
                    seq = r.text
                    sequence = seq[seq.index("\n"):]

                    context_html = {"gene": gene, "sequence": sequence}
                    context_json = {"gene": gene, "sequence": sequence.replace("\n", "")}

                    contents, content_type, error_code = su.json_or_html_return(arguments, context_html,
                                                                                context_json, html)

                else:
                    contents, content_type = su.read_html("./html/Error.html", "Gene not found in gene dict")
                    error_code = 404
            except KeyError as e:

                contents, content_type = su.read_html("./html/Error.html",
                                                      "Have to enter correct value in the parameter: " + str(e))
                error_code = 404
        elif path_name == "/geneInfo":
            try:
                gene = arguments["gene"][0]
                if gene in su.genes_dict:

                    id = su.genes_dict[gene]
                    ext_info = "/lookup/id/"
                    html = "./html/info_gene.html"

                    r = requests.get(server_info + ext_info + id + "?", headers={"Content-Type": "application/json"})

                    start = r.json()["start"]
                    end = r.json()["end"]
                    length = str(int(end) - int(start))
                    name = r.json()["assembly_name"]

                    context = {"gene": gene, "id": id, "start": start, "end": end, "length": length, "name": name}
                    contents, content_type, error_code = su.json_or_html_return(arguments, context, context, html)

                else:
                    contents, content_type = su.read_html("./html/Error.html", "Gene not found in gene dict")
                    error_code = 404
            except KeyError as e:

                contents, content_type = su.read_html("./html/Error.html",
                                                      "Have to enter correct value in the parameter: " + str(e))
                error_code = 404
        elif path_name == "/geneCalc":
            try:
                gene = arguments["gene"][0]
                if gene in su.genes_dict:
                    id = su.genes_dict[gene]
                    ext_info = "/lookup/id/"
                    html = "./html/calc_gene.html"

                    r = requests.get(server_info + ext_info + id + "?", headers={"Content-Type": "application/json"})

                    start = r.json()["start"]
                    end = r.json()["end"]
                    length = str(int(end) - int(start))

                    ext_seq = "/sequence/id/"

                    sequence = requests.get(server_info + ext_seq + id + "?content-type=text/plain")

                    base_perc = su.Seq(sequence.text).base_percentage()
                    base_perc_list = su.dict_to_list(base_perc)
                    base_perc_html = su.list_to_dot_html_list(base_perc_list)

                    context_html = {"gene": gene, "length": length, "base_perc": base_perc_html}
                    context_json = {"gene": gene, "length": length, "base_perc": base_perc}

                    contents, content_type, error_code = su.json_or_html_return(arguments, context_html,
                                                                                context_json, html)

                else:
                    contents, content_type = su.read_html("./html/Error.html", "Gene not found in gene dict")
                    error_code = 404
            except KeyError as e:

                contents, content_type = su.read_html("./html/Error.html",
                                                      "Have to enter correct value in the parameter: " + str(e))
                error_code = 404

        else:
            contents, content_type = su.read_html("./html/Error.html", "Endpoint not valid")
            error_code = 404

        # Generating the response message
        self.send_response(error_code)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', content_type)
        print(contents)
        self.send_header('Content-Length', str(len(contents.encode())))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler


Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new client, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
