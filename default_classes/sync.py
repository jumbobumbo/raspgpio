from startup_classes import connector
from startup_classes import json_reader as jr
from default_classes import data_handlers
from teardown.teardown import TearDown
from led import led_conn
from dirsync import sync
from pathlib import Path


class Syncer:
    def __init__(self, dir_key, regex, conf_path):
        """
        conf: Path object to config file
        dir_key: str - directories to sync (key from json file)
        regex: raw str - files to ignore in sync
        example: r".+\.(txt|log|git|jar)$"
        """
        self.dir_key = dir_key
        self.regex = regex
        self.conf_data = conf_path

    @property
    def conf_data(self):
        return self.__conf_data

    @conf_data.setter
    def conf_data(self, conf_path):
        self.__conf_data = jr.JSONReads(conf_path).json_data[self.dir_key]
