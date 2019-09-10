import os
import sys
from pathlib import Path
from startup_classes import connector, json_reader

# check to see if the Config DIR has more than one file in it
config_dir_list = os.listdir("./config")  # dir where config json files are stored
if len(config_dir_list) == 0:  # dir empty - we can't do anything
    print("no config files present, exiting")
    sys.exit(1)  # Goodnight
elif len(config_dir_list) == 1:  # use the only file present
    config_file = Path("./config", str(config_dir_list[0]))
else:  # we ask the user to choose a file
    try:
        u_input = int(input(f"Which file? (give me the integer value please):\n"
                            f"{[i for i in enumerate(config_dir_list)]}\n"))
        config_file = Path("./config", str(config_dir_list[u_input]))
    except (ValueError, IndexError) as ex:
        print(f"Input error: {ex}")
        sys.exit(1)  # Goodnight

"""
Connect and configure
All using the config file
"""
config_read = json_reader.JSONReads(config_file)
# find the connection IP add
ip_add = config_read.reader()["connection"]["ip_add"]
# connect to remote pi
conn_1_start = connector.PiConnect(ip_add)
conn_1 = conn_1_start.factory_connector()
