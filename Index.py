import cherrypy

class Index(object):

    @cherrypy.expose()
    def index(self):
        return open('index.html')

    @cherrypy.expose()
    def about(self):
        return """
               <html>
               <head><title>About Us</title></head>
               <body>
               <h1>About Us</h1>
               <p>This is our first python class.This is about us page</p>
               </body>
               </html>
               """


if __name__=='__main__':
    cherrypy.quickstart(Index())