import cherrypy

class SimplePage:
    @cherrypy.expose
    def index(self):
        with open("1267_12_07_html_document.html") as file:
            return file.read()

cherrypy.quickstart(SimplePage())
