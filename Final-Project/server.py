import http.server
import socketserver
from urllib.parse import urlparse, parse_qs
import server_utils as su

PORT = 8080
# Prevents error: port already in use
socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        o = urlparse(self.path)
        # get the endpoints
        path_name = o.path
        arguments = parse_qs(o.query)
        print("Resource requested: ", path_name)
        print("Parameters: ", arguments)
        server = "https://rest.ensembl.org"
        server_info = "https://grch37.rest.ensembl.org"

        # main page
        if path_name == "/":
            contents, content_type = su.read_html("./html/form.html", "")
            error_code = 200
        # list species
        elif path_name == "/listSpecies":
            ext = "/info/species?"
            html = "./html/list_of_species.html"
            contents, content_type, error_code = su.listSpecies(server, ext, arguments, html)

        # karyotype
        elif path_name == "/karyotype":
            ext = "/info/assembly/"
            html = "./html/karyotype.html"
            contents, content_type, error_code = su.karyotype(server, ext, arguments, html)

        # chromosomeLength
        elif path_name == "/chromosomeLength":

            ext = "/info/assembly/"
            html = "./html/len_chromo.html"
            contents, content_type, error_code = su.chromosomeLength(server, ext, arguments, html)

        # geneSeq
        elif path_name == "/geneSeq":
            ext = "/sequence/id/"
            html = "./html/sequence_gene.html"
            contents, content_type, error_code = su.geneSeq(server, ext, arguments, html)

        # geneInfo
        elif path_name == "/geneInfo":
            ext = "/lookup/id/"
            html = "./html/info_gene.html"
            contents, content_type, error_code = su.geneInfo(server_info, ext, arguments, html)

        # geneCalc
        elif path_name == "/geneCalc":

            ext = "/lookup/id/"
            html = "./html/calc_gene.html"
            contents, content_type, error_code = su.geneCalc(server_info, ext, arguments, html)

        else:
            contents, content_type = su.read_html("./html/Error.html", "Endpoint not valid")
            error_code = 404

        # response message
        self.send_response(error_code)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', content_type)
        print(contents)
        self.send_header('Content-Length', str(len(contents.encode())))

        # The header is finished
        self.end_headers()

        # response message
        self.wfile.write(contents.encode())

        return


# set the new handler


Handler = TestHandler

# open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # attend the client. Whenever there is a new client, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
