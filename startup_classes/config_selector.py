from pathlib import Path


class ConfSelect:

    @staticmethod
    def selection(config_f="default_config.json"):
        """ returns full path of conf file - blank means default"""
        return Path("./config", config_f)
