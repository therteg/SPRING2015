import app.basic
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import json

from lib.mongo import db
from lib import testmongo


class FBHandler(app.basic.BaseHandler):
	def my_callback(result, error):
		print 'result', repr(result)
	def get(self):
		self.render('index.html')

class CapricornHandler(app.basic.BaseHandler):
	def get(self):
		self.render('capricorn.html')
class AquariusHandler(app.basic.BaseHandler):
	def get(self):
		self.render('aquarius.html')
class PiscesHandler(app.basic.BaseHandler):
	def get(self):
		self.render('pisces.html')
class AriesHandler(app.basic.BaseHandler):
	def get(self):
		self.render('aries.html')
class TaurusHandler(app.basic.BaseHandler):
	def get(self):
		self.render('taurus.html')
class GeminiHandler(app.basic.BaseHandler):
	def get(self):
		self.render('gemini.html')
class CancerHandler(app.basic.BaseHandler):
	def get(self):
		self.render('cancer.html')
class LeoHandler(app.basic.BaseHandler):
	def get(self):
		self.render('leo.html')
class VirgoHandler(app.basic.BaseHandler):
	def get(self):
		self.render('virgo.html')
class LibraHandler(app.basic.BaseHandler):
	def get(self):
		self.render('libra.html')
class ScorpioHandler(app.basic.BaseHandler):
	def get(self):
		self.render('scorpio.html')
class SagittariusHandler(app.basic.BaseHandler):
	def get(self):
		self.render('sagittarius.html')