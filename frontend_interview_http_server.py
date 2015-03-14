from http.server import SimpleHTTPRequestHandler, HTTPServer
import http.server
import random
import json

display_choices = ["Different Tan",
        "Fate Amenable To Change",
        "Grey Area",
        "It's Character Forming",
        "Jaundiced Outlook",
        "Problem Child",
        "Reasonable Excuse",
        "Recent Convert",
        "Tactical Grace",
        "Unacceptable Behaviour",
        "Steely Glint",
        "Attitude Adjuster",
        "Frank Exchange Of Views",
        "Anticipation Of A New Lover's Arrival, The",
        "Death and Gravity",
        "Ethics Gradient",
        "Gunboat Diplomat"
        ]


class FrontendInterviewRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/get_update':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            
            req_data = {}
            req_data['item_id'] = random.randrange(100)
            req_data['selected'] = random.randrange(2)
            req_data['display'] = random.choice(display_choices)

            self.wfile.write(bytes(json.dumps(req_data), 'UTF-8'))
            
        else:
            return SimpleHTTPRequestHandler.do_GET(self)


if __name__ == '__main__':
    PORT = 7000
    server = HTTPServer(("0.0.0.0", PORT), FrontendInterviewRequestHandler)
    print("Serving at port", PORT)
    server.serve_forever()

