from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import urlfetch

class Fetch(webapp.RequestHandler):
    def get(self):
        url = self.request.get('url')
        callback = self.request.get('callback')
        result = urlfetch.fetch(url)
#        headers = result.headers
#        self.response.headers = headers
        self.response.headers.add_header('Access-Control-Allow-Origin', '*')
        self.response.set_status(result.status_code)
        content = result.content
        if callback != '':
            content = callback + '("' + content + '")'
        self.response.out.write(content)
application = webapp.WSGIApplication(
                                     [('/fetch', Fetch)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
    
