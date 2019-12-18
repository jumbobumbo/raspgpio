from startup_classes import json_reader as jr
from default_classes import data_handlers as dh
from startup_classes import connector
from led import led_conn as conn
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
    def conf_data(self, conf_path):  # returns the data as dict
        self.__conf_data = jr.JSONReads(conf_path).json_data

    def file_sync(self):
        """
        loop through key, values in self.conf_data dict
        """
        for source, dest in self.conf_data[self.dir_key].items():
            # start syncing
            sync(Path(source), Path(dest), "sync", verbose=False, exclude=(self.regex,))


class LEDSyncer(Syncer):
    def __init__(self, ip_key, LED_key, regex, dir_key, conf_data):
        """
        ip_key: key for ip address in Syncer.config_data
        LED_key: key for LED values in Syncer.config_data
        """
        self.ip_key = ip_key
        self.LED_key = LED_key
        super().__init__(regex, dir_key, conf_data)

    # limited to single rasp pi connection
    def file_sync_LED(self):
        """
        lights up LEDs on rasp pi and syncs listed DIRs
        """
        try:
            # open up the LED board connection (LED pin values, single pi conn obj)
            with conn.LED(dh.HandleData.dict_to_value_list(self.conf_data[self.LED_key]),
                          connector.PiConnect.single_factory_connector(self.conf_data[self.ip_key])).board() as pi:
                for i in [pi.blink, self.file_sync, pi.blink]:
                    i()  # blink, sync, blink
        except (IOError, OSError) as error:  # connection rejections
            print(f"{error} occurred when connecting to PI. Will sync without blink")
            self.file_sync()  # still sync the data
            # TODO: add handling of sync operation error
