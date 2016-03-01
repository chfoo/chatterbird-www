import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    pass


class BaseStaticHandler(tornado.web.StaticFileHandler):
    pass

