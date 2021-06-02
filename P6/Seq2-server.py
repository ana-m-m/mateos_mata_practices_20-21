import http.server
import socketserver
from urllib.parse import parse_qs, urlparse

import termcolor
import pathlib

import server_utils as su

def read_html_file(filename):
    content = pathlib.Path(filename).read_text()
    return content




# Define the Server's port
PORT = 8080
LIST_SEQUENCES = ["AGCTTTTT", "TTTTTTTT", "AAAACCCAA", "AGGGCACAAAT", "AAAGGTTTTA"]
LIST_GENES = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]

bases_information = {
    "A": {"Link":"https://en.wikipedia.org/wiki/Adenine", "formula": "C5H5N5","name": "ADENINE", "colour": "lightgreen"},
    "C": {"Link":"https://en.wikipedia.org/wiki/Citosine", "formula": "C4H5N3O","name": "CITOSINE", "colour": "yellow"},
    "T": {"Link":"https://en.wikipedia.org/wiki/Thymine", "formula": "C5H6N2O2","name": "THYMINE", "colour": "lightpink"},
    "G": {"Link":"https://en.wikipedia.org/wiki/Guanine", "formula": "C5H5N5O","name": "GUANINE", "colour": "lightblue"}
}

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, "blue")

        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print("Resource requested: ", path_name)
        print("Parameters: ", arguments)


        context = {}
        # Message to send back to the client
        try:
            if path_name == "/":
                context["n_sequences"] = len(LIST_SEQUENCES)
                context["list_genes"] = LIST_GENES

                contents = su.read_template_html_file("./html/form-4.html").render(context=context)

            elif path_name == "/test":
                contents = su.read_template_html_file("./html/test.html").render()
            elif path_name == "/ping":
                contents = su.read_template_html_file("./html/ping.html").render()
            elif path_name == "/get":
                number_sequence = arguments["sequence"][0]
                contents = su.get(LIST_SEQUENCES, number_sequence)
            elif path_name == "/gene":
                gene = arguments["gene"][0]
                contents = su.gene(gene)
            elif path_name == "/operate":
                sequence = arguments["sequence"][0]
                operation = arguments["operation"][0]
                if operation == "Info":
                    result = su.info(sequence)
                    contents = su.read_template_html_file("./html/operation.html").render(sequence=sequence,
                                                                                          operation=operation,
                                                                                          result=result)

                elif operation == "Comp":
                    result = su.comp(sequence)
                    contents = su.read_template_html_file("./html/operation.html").render(sequence=sequence,
                                                                                          operation=operation,
                                                                                          result=result)
                elif operation == "Rev":
                    result = su.rev(sequence)
                    contents = su.read_template_html_file("./html/operation.html").render(sequence=sequence,
                                                                                          operation=operation,
                                                                                          result=result)
            else:
                contents = su.read_template_html_file("./html/Error.html").render(context="")
        except KeyError as e:
            # keyerror aparece cuando falta un argumento
            contents = su.read_template_html_file("./html/Error.html").render(context=f"keyerror{e}")
        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
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

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
