import os

class Config(object):
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.database_dir = os.path.join(self.base_dir, "Big_DATA.csv")
        self.woeid_dir = os.path.join(self.base_dir, "WOEID.csv")

    def __str__(self):
        return "test?"

    def reset_database(self, dir):
        os.remove(dir)

    def database_exist(self, dir):
        return os.path.exists(dir)
