import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/content/'):
            # Serve the request normally for paths under /content
            super().do_GET()
        else:
            # Redirect all other requests to index.html
            self.path = '/index.html'
            return super().do_GET()

    def translate_path(self, path):
        """This method is used to translate a URL path to a local file path."""
        path = super().translate_path(path)
        # If path ends with a slash, it should point to the index.html in that directory.
        if path.endswith('/'):
            path = os.path.join(path, 'index.html')
        return path

if __name__ == "__main__":
    server_address = ('', 8000)  # Serve on all interfaces, port 8000
    httpd = HTTPServer(server_address, CustomHandler)
    print("Serving on port 8000...")
    httpd.serve_forever()
