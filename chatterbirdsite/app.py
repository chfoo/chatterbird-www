import os

from tornado.web import URLSpec as U
from tornado.web import HTTPError
import tornado.web
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


class BaseHandler(tornado.web.RequestHandler):
    pass


class BaseStaticHandler(tornado.web.StaticFileHandler):
    pass


class IndexHandler(BaseHandler):
    def get(self):
        self.render('index.html', run_infos=self.application.model.RUNS)


class ContactHandler(BaseHandler):
    def get(self):
        self.render('contact.html')


class RunHandler(BaseHandler):
    def get(self, slug):
        if slug not in self.application.model.RUN_MAP:
            raise HTTPError(404)

        self.render(
            'run.html',
            run_info=self.application.model.RUN_MAP[slug],
            recent_screenshots=self.application.model.get_recent_screenshots(slug)
        )


class ScreenshotImageHandler(BaseStaticHandler):
    @classmethod
    def get_absolute_path(cls, root, path):
        slug, dummy, filename = path.split('/', 3)
        date_str = filename[:10]
        path = os.path.join(root, slug, date_str, filename)
        return path


class ScreenshotListHandler(BaseHandler):
    def get(self, slug):
        if slug not in self.application.model.RUN_MAP:
            raise HTTPError(404)

        self.render(
            'screenshot_list.html',
            date_listing=self.application.model.get_screenshot_date_listing(slug),
            run_info=self.application.model.RUN_MAP[slug]
        )


class ScreenshotDateBrowseHandler(BaseHandler):
    def get(self, slug, date_str):
        if slug not in self.application.model.RUN_MAP:
            raise HTTPError(404)

        self.render(
            'screenshot_date_browse.html',
            date_str=date_str,
            filenames=self.application.model.get_screenshot_filename_listing(slug, date_str),
            run_info=self.application.model.RUN_MAP[slug]
        )
