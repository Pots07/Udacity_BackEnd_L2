import os

import jinja2
import webapp2

#templates directory sub-directory of current directory
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
#look for templates here:
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
							   autoescape = True)


class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):	#*a variable no of arg
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)	#load file that is the template
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class MainPage(Handler):
	def get(self):
		items = self.request.get_all("food")
		self.render("shopping_list.html", items = items)

class FizzBuzzHandler(Handler):
	def get(self):
		n = self.request.get('n', 0)
		n = n and int(n)
		self.render('FizzBuzz.html', n = n)

app = webapp2.WSGIApplication([('/', MainPage),
							   ('/FizzBuzz', FizzBuzzHandler)
							  ],debug=True)
