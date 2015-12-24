import datetime
import tornado.web

class Thumbnail(tornado.web.UIModule):
    def render(self, slug, image_filename):
        thumbnail_date = datetime.datetime.strptime(image_filename[:19], '%Y-%m-%d_%H-%M-%S')

        return self.render_string(
            'thumbnail_module.html', slug=slug, filename=image_filename,
            thumbnail_date=thumbnail_date
        )
