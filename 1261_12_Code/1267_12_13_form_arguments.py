import cherrypy

class ContactPage:
    @cherrypy.expose
    def index(self, message=None):
        if message:
            print("The user submitted:\n{0}".format(
                message))
            return "Thank you!"
        return """<form>
            <textarea name="message"></textarea>
            <input type="submit" />
            </form>"""

cherrypy.quickstart(ContactPage())
