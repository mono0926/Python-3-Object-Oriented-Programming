import cherrypy

template = """<!DOCTYPE html>
<html>
    <body>
        {message}
    </body>
</html>"""

class AboutPage:
    @cherrypy.expose
    def index(self):
        return template.format(message="""
        I'm not a very interesting person...""")

@cherrypy.expose
def contactPage(self):
    print(self)
    return template.format(
            message="I can't be contacted anywhere.")

class MainPage:
    about = AboutPage()
    contact = contactPage
    @cherrypy.expose
    def index(self):
        return template.format(message="""
        This is the main page.
        <a href="/about/">About Me</a>
        <a href="/contact/">Contact Me</a>
        <a href="/links/">Some Links</a>
        """)

    @cherrypy.expose
    def links(self):
        return template.format(
                message="No Links Yet")

cherrypy.quickstart(MainPage())
