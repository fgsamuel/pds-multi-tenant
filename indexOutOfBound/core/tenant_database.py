from django.conf import settings


class Database(dict):
    cache = {}

    def __getitem__(self, item):
        if item not in self.cache:
            self.cache[item] = {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': str(settings.BASE_DIR / f'{item}.db.sqlite3'),
            }
        return self.cache[item]

    def __contains__(self, item):
        return True
