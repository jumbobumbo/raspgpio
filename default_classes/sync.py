from startup_classes import json_reader as jr
from dirsync import sync
from pathlib import Path


class Syncer:
    def __init__(self, regex, dir_key, conf_path):
        """
        regex: raw str - files to ignore in sync - example: r".+\.(txt|log|git|jar)$"
        dir_key: key from json file (directories to sync)
        conf: Path object to config file
        """
        self.regex = regex
        self.dir_key = dir_key
        self.conf_data = conf_path

    @property
    def conf_data(self):
        return self.__conf_data

    @conf_data.setter
    def conf_data(self, conf_path):  # returns the key values
        self.__conf_data = jr.JSONReads(conf_path).json_data[self.dir_key]

    def start_sync(self):
        """
        loop through key, values in self.conf_data dict
        """
        for source, dest in self.conf_data.items():
            # start syncing
            sync(Path(source), Path(dest), "sync", verbose=False, exclude=(self.regex,))
