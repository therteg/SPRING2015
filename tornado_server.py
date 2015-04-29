import os
import tornado.httpserver
import tornado.httpclient
import tornado.ioloop
import tornado.options
import tornado.web

import logging

# settings is required/used to set our environment
import settings 

import app.basic
import app.general



handlers = handlers = [
    (r"/", app.general.HomeHandler),
    (r"/capricorn", app.general.CapricornHandler),
    (r"/aquarius", app.general.AquariusHandler),
    (r"/pisces", app.general.PiscesHandler),
    (r"/aries", app.general.AriesHandler),
    (r"/taurus", app.general.TaurusHandler),
    (r"/gemini", app.general.GeminiHandler),
    (r"/cancer", app.general.CancerHandler),
    (r"/leo", app.general.LeoHandler),
    (r"/virgo", app.general.VirgoHandler),
    (r"/libra", app.general.LibraHandler),
    (r"/scorpio", app.general.ScorpioHandler),
    (r"/sagittarius", app.general.SagittariusHandler),

    (r"/capricorn/explore", app.general.CapricornExploreHandler),
    (r"/aquarius/explore", app.general.AquariusExploreHandler),
    (r"/pisces/explore", app.general.PiscesExploreHandler),
    (r"/aries/explore", app.general.AriesExploreHandler),
    (r"/taurus/explore", app.general.TaurusExploreHandler),
    (r"/gemini/explore", app.general.GeminiExploreHandler),
    (r"/cancer/explore", app.general.CancerExploreHandler),
    (r"/leo/explore", app.general.LeoExploreHandler),
    (r"/virgo/explore", app.general.VirgoExploreHandler),
    (r"/libra/explore", app.general.LibraExploreHandler),
    (r"/scorpio/explore", app.general.ScorpioExploreHandler),
    (r"/sagittarius/explore", app.general.SagittariusExploreHandler),

    (r"/capricorn/compatibility", app.general.CapricornCompatibilityHandler),
    (r"/aquarius/compatibility", app.general.AquariusCompatibilityHandler),
    (r"/pisces/compatibility", app.general.PiscesCompatibilityHandler),
    (r"/aries/compatibility", app.general.AriesCompatibilityHandler),
    (r"/taurus/compatibility", app.general.TaurusCompatibilityHandler),
    (r"/gemini/compatibility", app.general.GeminiCompatibilityHandler),
    (r"/cancer/compatibility", app.general.CancerCompatibilityHandler),
    (r"/leo/compatibility", app.general.LeoCompatibilityHandler),
    (r"/virgo/compatibility", app.general.VirgoCompatibilityHandler),
    (r"/libra/compatibility", app.general.LibraCompatibilityHandler),
    (r"/scorpio/compatibility", app.general.ScorpioCompatibilityHandler),
    (r"/sagittarius/compatibility", app.general.SagittariusCompatibilityHandler),

    (r"/capricorn/famous", app.general.CapricornFamousHandler),
    (r"/aquarius/famous", app.general.AquariusFamousHandler),
    (r"/pisces/famous", app.general.PiscesFamousHandler),
    (r"/aries/famous", app.general.AriesFamousHandler),
    (r"/taurus/famous", app.general.TaurusFamousHandler),
    (r"/gemini/famous", app.general.GeminiFamousHandler),
    (r"/cancer/famous", app.general.CancerFamousHandler),
    (r"/leo/famous", app.general.LeoFamousHandler),
    (r"/virgo/famous", app.general.VirgoFamousHandler),
    (r"/libra/famous", app.general.LibraFamousHandler),
    (r"/scorpio/famous", app.general.ScorpioFamousHandler),
    (r"/sagittarius/famous", app.general.SagittariusFamousHandler),
]


settings = dict(
        cookie_secret="change_me",
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
) 
              

application = tornado.web.Application(handlers, **settings)

if __name__ == "__main__":
    port = os.environ['PORT'] if os.environ['PORT'] else 8888
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()