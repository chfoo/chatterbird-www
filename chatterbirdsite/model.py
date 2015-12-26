import datetime
import glob
import os


class AppModel(object):
    RUNS = [
        {
            'slug': 'aiss-psmd',
            'title': 'Twitch Plays Pokémon Super Mystery Dungeon (By Aissurtievos)',
            'run_start': datetime.datetime(2015, 12, 26, 17, 00, tzinfo=datetime.timezone.utc),
            'url': 'http://www.twitch.tv/aissurtievos'
        }
    ]

    RUN_MAP = {}
    for run_info in RUNS:
        RUN_MAP[run_info['slug']] = run_info

    def __init__(self, app):
        self._app = app

    def get_screenshots_dir(self):
        return os.path.join(
            os.path.abspath(self._app.config['data_dir']), 'screenshots'
        )

    def get_screenshot_date_listing(self, slug):
        screenshots_path = os.path.join(self.get_screenshots_dir(), slug)
        listing = sorted(os.listdir(screenshots_path))

        return listing

    def get_screenshot_filename_listing(self, slug, date_str):
        screenshots_path = os.path.join(self.get_screenshots_dir(), slug)
        directory_path = os.path.join(screenshots_path, date_str)
        pattern = directory_path + '/[0-9]*[0-9].jpg'

        return sorted(os.path.basename(path) for path in glob.glob(pattern))

    def get_recent_screenshots(self, slug, count=5):
        image_filenames = []
        date_strs = reversed(self.get_screenshot_date_listing(slug))

        for date_str in date_strs:
            filename_listing = reversed(self.get_screenshot_filename_listing(slug, date_str))

            for filename in filename_listing:
                image_filenames.append(filename)

                if len(image_filenames) >= count:
                    return image_filenames

        return image_filenames