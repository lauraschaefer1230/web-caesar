
import webapp2
import caesar
import cgi

def build_page(textareacontent):
        rot_label = "<label>Rotate by:</label>"
        message_label = "<label>Type a message</label>"
        rotation_input = "<input type='number' name='rotation'/>"
        textarea = "<textarea name='message'>" + textareacontent + "</textarea>"
        submit = "<input type='submit'/>"
        form = "<form method='post'>" + rot_label + rotation_input + "<br>" + message_label + textarea + "<br>" +submit + "</form>"
        header = "<h2>Web Caesar</h2>"
        return header + form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #message = "Hello, World!"
        #encrypted_message = caesar.encrypt(message, 13)
        content = build_page("")
        #form = "<form method='post'>" + rot_label + rotation_input + "<br>" + message_label + textarea + "<br>" +submit + "</form>"
        self.response.write(content)

    def post(self):
        message = self.request.get("message")
        rotation = int(self.request.get("rotation"))
        encrypted_message = caesar.encrypt(message, rotation)
        escaped_message = cgi.escape(encrypted_message)

        content = build_page(escaped_message)
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
