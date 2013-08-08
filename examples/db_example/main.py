import boot
boot.setup()

import webapp2


class HelloWorldHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('Hello world!')


# Setup your jinja path.
config = {
    'webapp2_extras.jinja2': {
        'template_path': 'templates'
    }
}

app = webapp2.WSGIApplication(
    [('/', HelloWorldHandler)],
    config=config
)
