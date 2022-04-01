import dj_database_url


class Database(dict):
    cache = {}

    def __getitem__(self, item):
        if item not in self.cache:
            try:
                self.cache[item] = dj_database_url.config(default=item)
            except:
                self.cache[item] = dj_database_url.config(default="sqlite:///default.com.br.sqlite3")

        return self.cache[item]

    def __contains__(self, item):
        return True
