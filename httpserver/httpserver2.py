# source from https://pythonbasics.org/webserver/

# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer

from lib import db
from lib import functions

hostName = "localhost"
serverPort = 80


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        if self.path == "/hallo":
            filename = "templates/hallo.html"
        elif self.path == "/":
            filename = "templates/index.html"
        elif self.path == "/films":
            filename = "templates/films.html"
        else:
            filename = ""

        if filename == "":
            self.send_response(404)
            self.end_headers()
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            f = open(filename, "r")
            output = ""
            for line in f:
                output += (line.strip())

            films = db.GetData("select film_id, title, description from film")
            films_html = functions.DicttoHTML_Films(films)
            output = output.replace("$$films$$", films_html)

            self.wfile.write(bytes(output, "utf-8"))





if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
