import app.basic
<<<<<<< HEAD
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import json

from lib.mongo import db
from lib import testmongo
=======
#from apiclient.discovery import build
#from apiclient.errors import HttpError
#from oauth2client.tools import argparser
#import json

#from lib.mongo import db
#from lib import testmongo
>>>>>>> 3b7a0a9ba1c5ec0f9f8fb49b80fcf54db3f583c1


class HomeHandler(app.basic.BaseHandler):
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


class CapricornExploreHandler(app.basic.BaseHandler):
	def get(self):
		self.render('overview-capricorn.html')
class AquariusExploreHandler(app.basic.BaseHandler):
	def get(self):
		self.render('overview-aquarius.html')
class PiscesExploreHandler(app.basic.BaseHandler):
	def get(self):
		self.render('overview-pisces.html')
class AriesExploreHandler(app.basic.BaseHandler):
	def get(self):
		self.render('overview-aries.html')
class TaurusExploreHandler(app.basic.BaseHandler):
	def get(self):
		self.render('overview-taurus.html')
class GeminiExploreHandler(app.basic.BaseHandler):
	def get(self):
		self.render('overview-gemini.html')
class CancerExploreHandler(app.basic.BaseHandler):
	def get(self):
		self.render('overview-cancer.html')
class LeoExploreHandler(app.basic.BaseHandler):
	def get(self):
		self.render('overview-leo.html')
class VirgoExploreHandler(app.basic.BaseHandler):
	def get(self):
		self.render('overview-virgo.html')
class LibraExploreHandler(app.basic.BaseHandler):
	def get(self):
		self.render('overview-libra.html')
class ScorpioExploreHandler(app.basic.BaseHandler):
	def get(self):
		self.render('overview-scorpio.html')
class SagittariusExploreHandler(app.basic.BaseHandler):
	def get(self):
		self.render('overview-sagittarius.html')

class CapricornCompatibilityHandler(app.basic.BaseHandler):
	def get(self):
		self.render('compatibility-capricorn.html')
class AquariusCompatibilityHandler(app.basic.BaseHandler):
	def get(self):
		self.render('compatibility-aquarius.html')
class PiscesCompatibilityHandler(app.basic.BaseHandler):
	def get(self):
		self.render('compatibility-pisces.html')
class AriesCompatibilityHandler(app.basic.BaseHandler):
	def get(self):
		self.render('compatibility-aries.html')
class TaurusCompatibilityHandler(app.basic.BaseHandler):
	def get(self):
		self.render('compatibility-taurus.html')
class GeminiCompatibilityHandler(app.basic.BaseHandler):
	def get(self):
		self.render('compatibility-gemini.html')
class CancerCompatibilityHandler(app.basic.BaseHandler):
	def get(self):
		self.render('compatibility-cancer.html')
class LeoCompatibilityHandler(app.basic.BaseHandler):
	def get(self):
		self.render('compatibility-leo.html')
class VirgoCompatibilityHandler(app.basic.BaseHandler):
	def get(self):
		self.render('compatibility-virgo.html')
class LibraCompatibilityHandler(app.basic.BaseHandler):
	def get(self):
		self.render('compatibility-libra.html')
class ScorpioCompatibilityHandler(app.basic.BaseHandler):
	def get(self):
		self.render('compatibility-scorpio.html')
class SagittariusCompatibilityHandler(app.basic.BaseHandler):
	def get(self):
		self.render('compatibility-sagittarius.html')

class CapricornFamousHandler(app.basic.BaseHandler):
	def get(self):
		self.render('famous-capricorn.html')
class AquariusFamousHandler(app.basic.BaseHandler):
	def get(self):
		self.render('famous-aquarius.html')
class PiscesFamousHandler(app.basic.BaseHandler):
	def get(self):
		self.render('famous-pisces.html')
class AriesFamousHandler(app.basic.BaseHandler):
	def get(self):
		self.render('famous-aries.html')
class TaurusFamousHandler(app.basic.BaseHandler):
	def get(self):
		self.render('famous-taurus.html')
class GeminiFamousHandler(app.basic.BaseHandler):
	def get(self):
		self.render('famous-gemini.html')
class CancerFamousHandler(app.basic.BaseHandler):
	def get(self):
		self.render('famous-cancer.html')
class LeoFamousHandler(app.basic.BaseHandler):
	def get(self):
		self.render('famous-leo.html')
class VirgoFamousHandler(app.basic.BaseHandler):
	def get(self):
		self.render('famous-virgo.html')
class LibraFamousHandler(app.basic.BaseHandler):
	def get(self):
		self.render('famous-libra.html')
class ScorpioFamousHandler(app.basic.BaseHandler):
	def get(self):
		self.render('famous-scorpio.html')
class SagittariusFamousHandler(app.basic.BaseHandler):
	def get(self):
		self.render('famous-sagittarius.html')