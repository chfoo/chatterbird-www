import os

from tornado.web import URLSpec as U
import tornado.web

from chatterbirdsite.handlers.base import BaseHandler
from chatterbirdsite.handlers.screenshot import RunHandler, \
    ScreenshotListHandler, ScreenshotDateBrowseHandler, ScreenshotImageHandler
from chatterbirdsite.model import AppModel
import chatterbirdsite.uimodules


class App(tornado.web.Application):
    def __init__(self, config):
        self.config = config
        self.model = AppModel(self)
        super().__init__(
            [
                U(r'/', IndexHandler, name='index'),
                U(r'/contact', ContactHandler, name='contact'),
                U(r'/run/([a-zA-Z0-9_-]+)', RunHandler, name='run'),
                U(r'/run/([a-zA-Z0-9_-]+)/screenshot/list',
                  ScreenshotListHandler, name='run.screenshot.list'),
                U(r'/run/([a-zA-Z0-9_-]+)/screenshot/(\d{4}-\d{2}-\d{2})',
                  ScreenshotDateBrowseHandler, name='run.screenshot.date_browse'),
                U(r'/run/([a-zA-Z0-9_-]+/screenshot/\d[a-z\d_-]+.jpg)',
                  ScreenshotImageHandler,
                  {'path': self.model.get_screenshots_dir()},
                  name='run.screenshot.image',
                ),
            ],
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            ui_modules=chatterbirdsite.uimodules,
            static_path=os.path.join(os.path.dirname(__file__), 'static')
        )


class IndexHandler(BaseHandler):
    def get(self):
        self.render('index.html', run_infos=self.application.model.RUNS)


class ContactHandler(BaseHandler):
    def get(self):
        self.render('contact.html')
