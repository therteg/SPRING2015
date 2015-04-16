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

from pyechonest import config
config.ECHO_NEST_API_KEY="CGR1FESZMSLL0AITW"

class Application(tornado.web.Application):
    def __init__(self):
        debug = (tornado.options.options.environment == "dev")

        app_settings = {
            "cookie_secret" : "change_me",
            "login_url": "/",
            "debug": debug,
            "static_path" : os.path.join(os.path.dirname(__file__), "static"),
            "template_path" : os.path.join(os.path.dirname(__file__), "templates"),
        }

        """
        the endpoints this torando instance provides
        """
        handlers = [
            (r"/", app.general.FBHandler),
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
        ]

        tornado.web.Application.__init__(self, handlers, **app_settings)

def main():
    tornado.options.define("port", default=8001, help="Listen on port", type=int)
    tornado.options.parse_command_line()
    logging.info("starting tornado_server on 0.0.0.0:%d" % tornado.options.options.port)
    http_server = tornado.httpserver.HTTPServer(request_callback=Application(), xheaders=True)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
