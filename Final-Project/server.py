import http.server
import pathlib
import socketserver
from urllib.parse import urlparse, parse_qs

from jinja2 import Template
import requests, sys


def read_template_html_file(filename):
    content = Template(pathlib.Path(filename).read_text())
    return content


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

        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok

        if path_name == "/":
            contents = read_template_html_file("./html/form.html").render(context="")
        elif path_name == "/listSpecies":
            ext = "/info/species?"
            try:
                r = requests.get(server + ext, headers={"Content-Type": "application/json"})
                if not r.ok:
                    r.raise_for_status()
                    sys.exit()
                dict_species = r.json()["species"]
                if arguments == {}:
                    species = []
                    for i in range(0, len(dict_species)):
                        species.append(dict_species[i]["name"])
                    contents = read_template_html_file("./html/list of species.html").render(tot_species=len(dict_species),
                                                                                             limit= "NONE",
                                                                                             species=species)
                else:
                    limit = arguments["limit"][0]
                    species = []
                    for i in range(0,int(limit)):
                        species.append(dict_species[i]["name"])

                    contents = read_template_html_file("./html/list of species.html").render(tot_species=len(dict_species),
                                                                                             limit=limit,
                                                                                             species=species)
            except Exception as e:
                contents = read_template_html_file("./html/Error.html").render(error = e)
        elif path_name == "/karyotype":
            ext = "/info/assembly/"
            specie = arguments["specie"][0]
            try:
                r = requests.get(server + ext + specie + "?", headers={"Content-Type": "application/json"})

                if not r.ok:
                    r.raise_for_status()
                    sys.exit()
                karyotype = r.json()["karyotype"]
                contents = read_template_html_file("./html/karyotype.html").render(karyotype=karyotype)
            except Exception as e:
                contents = read_template_html_file("./html/Error.html").render(error = e)
        elif path_name == "/chromosomeLength":
            specie = arguments["specie"][0]
            chromo = arguments["chromo"][0]
            ext = "/info/assembly/"
            try:
                r = requests.get(server + ext + specie + "?", headers={"Content-Type": "application/json"})
                if not r.ok:
                    r.raise_for_status()
                    sys.exit()
                chromosomes = r.json()["top_level_region"]
                for chromosome in chromosomes:
                    if chromosome["name"] == chromo:
                        chromo_len = chromosome["length"]
                contents = read_template_html_file("./html/len_chromo.html").render(chromo_len=chromo_len)
            except Exception as e:
                contents = read_template_html_file("./html/Error.html").render(error = e)



        else:
            contents = read_template_html_file("./html/Error.html").render(error = "")
        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

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
