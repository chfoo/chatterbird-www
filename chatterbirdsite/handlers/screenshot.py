import os

from tornado.web import HTTPError

from chatterbirdsite.handlers.base import BaseHandler, BaseStaticHandler


class RunHandler(BaseHandler):
    def get(self, slug):
        if slug not in self.application.model.RUN_MAP:
            raise HTTPError(404)

        self.render(
            'run.html',
            run_info=self.application.model.RUN_MAP[slug],
            recent_screenshots=self.application.model.get_recent_screenshots(slug)
        )


class ScreenshotUnavailableMixin:
    def render_unavailable(self, slug):
        self.set_status(404)
        self.render(
            'images_not_available.html',
            run_info=self.application.model.RUN_MAP[slug]
        )
        return


class ScreenshotImageHandler(BaseStaticHandler, ScreenshotUnavailableMixin):
    @classmethod
    def get_absolute_path(cls, root, path):
        slug, dummy, filename = path.split('/', 3)
        date_str = filename[:10]
        path = os.path.join(root, slug, date_str, filename)
        return path

    def write_error(self, status_code, **kwargs):
        dummy, slug, dummy2 = self.request.path.strip('/').split('/', 2)

        if status_code == 404 and self.application.model.is_screenshots_unavailable(slug):
            self.render_unavailable(slug)
            return
        else:
            super().write_error(status_code, **kwargs)


class ScreenshotListHandler(BaseHandler, ScreenshotUnavailableMixin):
    def get(self, slug):
        if slug not in self.application.model.RUN_MAP:
            raise HTTPError(404)

        if self.application.model.is_screenshots_unavailable(slug):
            self.render_unavailable(slug)
            return

        self.render(
            'screenshot_list.html',
            date_listing=reversed(self.application.model.get_screenshot_date_listing(slug)),
            run_info=self.application.model.RUN_MAP[slug]
        )


class ScreenshotDateBrowseHandler(BaseHandler, ScreenshotUnavailableMixin):
    def get(self, slug, date_str):
        if slug not in self.application.model.RUN_MAP:
            raise HTTPError(404)

        if self.application.model.is_screenshots_unavailable(slug):
            self.render_unavailable(slug)
            return

        self.render(
            'screenshot_date_browse.html',
            date_str=date_str,
            filenames=reversed(self.application.model.get_screenshot_filename_listing(slug, date_str)),
            run_info=self.application.model.RUN_MAP[slug]
        )
