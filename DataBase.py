from Utils import *
import pandas as pd

config = Config()

class DataBase(object):

    def __init__(self, dir, base_columns):
        print("Setting up configurations...")
        self.dir = dir
        self.base_columns = base_columns
        if config.database_exist(self.dir):
            print("database found, attempting to recover database...")
            self.df = pd.read_csv(self.dir)
            print("database recovered!")
        else:
            print("attempting to create database...")
            self.df = self.initialize_csv()
        print("DataBase created!")

    def initialize_csv(self):
        base_columns_dict = dict()
        for thing in self.base_columns:
            base_columns_dict[thing] = []
        file_name = self.dir
        df = pd.DataFrame(base_columns_dict)
        df.to_csv(file_name)
        return df

    def reset(self):
        config.reset_database(self.dir)
        self.df = self.initialize_csv()

    def save(self):
        self.df.to_csv(self.dir)

    # stats is a list similar to containing values for base_columns
    # name is the row?
    def update_row(self, stats):
        self.df = self.df.append(stats, ignore_index=True)

# example of how to update stuff

if __name__ == "__main__":
    base_columns = ["name", "country", "woeid"]
    d1 = DataBase(config.woeid_dir, base_columns)
    d1.reset()
    d1.update_row({"name": "test", "woeid": 123, "country": "fam"})
    print(d1.df)
    d1.save()
    base_columns = ["tweet", "user", "likes", "retweets"]
    d2 = DataBase(config.database_dir, base_columns)