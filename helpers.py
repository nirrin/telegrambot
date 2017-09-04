from os import urandom
from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader('login', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

login_template = env.get_template('login.html')

def generate_secret():
	return str(int(urandom(4).encode('hex'), 16))

def login_message(secret):
	return login_template.render(secret=secret)