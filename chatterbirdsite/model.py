import datetime
import glob
import os


class AppModel(object):
    RUNS = [
        {
            'slug': 'tpp-post-rand-white-2',
            'title': 'TwitchPlaysPokemon Post Randomized White 2',
            'run_start': datetime.datetime(2017, 6, 21, 19, 0, tzinfo=datetime.timezone.utc),
            'url': 'http://www.twitch.tv/twitchplayspokemon'
        },
        {
            'slug': 'tpp-rand-white-2',
            'title': 'TwitchPlaysPokemon Randomized White 2',
            'run_start': datetime.datetime(2017, 6, 3, 21, 0, tzinfo=datetime.timezone.utc),
            'url': 'http://www.twitch.tv/twitchplayspokemon'
        },
        {
            'slug': 'tpp-post-blazed-glazed',
            'title': 'TwitchPlaysPokemon Post Blazed Glazed',
            'run_start': datetime.datetime(2017, 4, 8, 16, 0, tzinfo=datetime.timezone.utc),
            'url': 'http://www.twitch.tv/twitchplayspokemon'
        },
        {
            'slug': 'tpp-blazed-glazed',
            'title': 'TwitchPlaysPokemon Blazed Glazed',
            'run_start': datetime.datetime(2017, 4, 8, 16, 0, tzinfo=datetime.timezone.utc),
            'url': 'http://www.twitch.tv/twitchplayspokemon'
        },
        {
            'slug': 'tpp-post-ani-2017',
            'title': 'TwitchPlaysPokemon Post 2017 Anniversary',
            'run_start': datetime.datetime(2017, 2, 24, 16, 0, tzinfo=datetime.timezone.utc),
            'url': 'http://www.twitch.tv/twitchplayspokemon',
            'download_link': 'https://archive.org/details/tpp-post-ani-2017-screenshots'
        },
        {
            'slug': 'tpp-ani-2017',
            'title': 'TwitchPlaysPokemon 2017 Anniversary',
            'run_start': datetime.datetime(2017, 2, 12, 21, 0, tzinfo=datetime.timezone.utc),
            'url': 'http://www.twitch.tv/twitchplayspokemon',
            'download_link': 'https://archive.org/details/tpp-ani-2017-chatty-yellow-screenshots',
        },
        {
            'slug': 'tpp-post-waning-moon',
            'title': 'TwitchPlaysPokemon Post Waning Moon',
            'run_start': datetime.datetime(2017, 1, 27, 6, 0, tzinfo=datetime.timezone.utc),
            'url': 'http://www.twitch.tv/twitchplayspokemon',
            'download_link': 'https://archive.org/details/tpp-post-waning-moon',
        },
        {
            'slug': 'tpp-waning-moon',
            'title': 'TwitchPlaysPokemon Waning Moon',
            'run_start': datetime.datetime(2017, 1, 13, 18, 0, tzinfo=datetime.timezone.utc),
            'url': 'http://www.twitch.tv/twitchplayspokemon',
            'download_link': 'https://archive.org/details/tpp-waning-moon-screenshots',
        },
        {
            'slug': 'tpp-post-sun',
            'title': 'TwitchPlaysPokemon Post-Sun',
            'run_start': datetime.datetime(2016, 12, 2, 22, 0, tzinfo=datetime.timezone.utc),
            'url': 'http://www.twitch.tv/twitchplayspokemon',
            'download_link': 'https://archive.org/details/tpp-post-sun-screenshots',
        },
        {
            'slug': 'tpp-sun',
            'title': 'TwitchPlaysPokemon Sun',
            'run_start': datetime.datetime(2016, 11, 19, 22, 0, tzinfo=datetime.timezone.utc),
            'url': 'http://www.twitch.tv/twitchplayspokemon',
            'download_link': 'https://archive.org/details/tpp-sun-screenshots'
        },
        {
            'slug': 'tpp-post-prism',
            'title': 'TwitchPlaysPokemon Post Prism',
            'run_start': datetime.datetime(2016, 10, 9, 21, 0, tzinfo=datetime.timezone.utc),
            'url': 'http://www.twitch.tv/twitchplayspokemon',
            'download_link': 'https://archive.org/details/tpp-post-prism-screenshots'
        },
        {
            'slug': 'tpp-prism',
            'title': 'TwitchPlaysPokemon Prism',
            'run_start': datetime.datetime(2016, 10, 9, 21, 0, tzinfo=datetime.timezone.utc),
            'url': 'http://www.twitch.tv/twitchplayspokemon',
            'download_link': 'https://archive.org/download/tpp-prism-screenshots'
        },
        {
            'slug': 'tpp-post-rand-plat',
            'title': 'TwitchPlaysPokemon Post Randomized Platinum',
            'run_start': datetime.datetime(2016, 7, 31, 21, 0, tzinfo=datetime.timezone.utc),
            'url': 'http://www.twitch.tv/twitchplayspokemon',
            'download_link': 'https://archive.org/details/tpp-post-rand-plat-screenshots',
        },
        {
            'slug': 'tpp-rand-plat',
            'title': 'Twitch Plays Randomized Platinum (By TwitchPlaysPokemon)',
            'run_start': datetime.datetime(2016, 7, 31, 21, 0, tzinfo=datetime.timezone.utc),
            'url': 'http://www.twitch.tv/twitchplayspokemon',
            'download_link': 'https://archive.org/details/tpp-rand-plat-screenshots',
        },
        {
            'slug': 'tpp-brown',
            'title': 'Twitch Plays Pokemon Brown (By TwitchPlaysPokemon)',
            'run_start': datetime.datetime(2016, 6, 19, 21, 0, tzinfo=datetime.timezone.utc),
            'url': 'http://www.twitch.tv/twitchplayspokemon',
            'download_link': 'https://archive.org/details/tpp-brown-screenshots'
        },
        {
            'slug': 'aiss-dual-test',
            'title': 'Misc dual game test (Aissurtievos)',
            'run_start': datetime.datetime(2016, 4, 24, 19, 0, tzinfo=datetime.timezone.utc),
            'url': 'http://www.twitch.tv/aissurtievos'
        },
        {
            'slug': 'tpp-telefang',
            'title': 'Twitch Plays "Pokémon Diamond" Telefang (By TwitchPlaysPokemon)',
            'run_start': datetime.datetime(2016, 3, 16, 21, 0, tzinfo=datetime.timezone.utc),
            'url': 'http://www.twitch.tv/twitchplayspokemon',
            'download_link': 'https://archive.org/details/tpp-telefang-screenshots',
        },
        {
            'slug': 'tpp-crystal-251',
            'title': 'Twitch Plays Pokémon Anniversary Crystal 251 (By TwitchPlaysPokemon)',
            'run_start': datetime.datetime(2016, 2, 14, 21, 0, tzinfo=datetime.timezone.utc),
            'url': 'http://www.twitch.tv/twitchplayspokemon',
            'download_link': 'https://archive.org/details/tpp-ac-screenshots',
        },
        {
            'slug': 'aoc-2016-01-30',
            'title': 'AoC #8: Twitch Plays Surgeon Sim, Twitch Does Your Homework, Twitch makes a promo for the next TPP run, other weird things... (By AdventuresOfChat)',
            'run_start': datetime.datetime(2016, 1, 31, 1, 0, tzinfo=datetime.timezone.utc),
            'url': 'http://www.twitch.tv/AdventuresOfChat'
        },
        {
            'slug': 'aoc-2016-01-09',
            'title': 'Twitch Flies A Plane, Twitch Plays Flash Games, <top-secret thing> (By AdventuresOfChat)',
            'run_start': datetime.datetime(2016, 1, 10, 1, 0, tzinfo=datetime.timezone.utc),
            'url': 'http://www.twitch.tv/AdventuresOfChat'
        },
        {
            'slug': 'aiss-psmd-post',
            'title': 'PSMD post game misc (Aissurtievos)',
            'run_start': datetime.datetime(2016, 1, 10, 0, 0, tzinfo=datetime.timezone.utc),
            'url': 'http://www.twitch.tv/aissurtievos'
        },
        {
            'slug': 'aiss-psmd',
            'title': 'Twitch Plays Pokémon Super Mystery Dungeon (By Aissurtievos)',
            'run_start': datetime.datetime(2015, 12, 26, 17, 0, tzinfo=datetime.timezone.utc),
            'url': 'http://www.twitch.tv/aissurtievos'
        },
        {
            'slug': 'aiss-psmd-pre',
            'title': 'Testing (Aissurtievos)',
            'run_start': datetime.datetime(2015, 12, 24, 0, 0, tzinfo=datetime.timezone.utc),
            'url': 'http://www.twitch.tv/aissurtievos'
        },
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

    def is_screenshots_unavailable(self, slug):
        if slug not in self.RUN_MAP:
            return False

        recent = self.get_recent_screenshots(slug, count=1)

        return not recent and self.RUN_MAP[slug].get('download_link')
