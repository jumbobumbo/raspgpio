from startup_classes import connector, json_reader, config_selector
from default_classes import data_handlers
from teardown.teardown import TearDown
from led import led_conn
from dirsync import sync
from pathlib import Path


""" FILE SYNC CONFIG """
# regex for ignore files
regex = r".+\.(txt|log|git|jar)$"  # populated examples
# DIRECTORIES
dirs = {
        "c:/Users/dbwheeler/Documents/Cities_Skylines": "c:/Users/dbwheeler/Documents/dumps2"
}

""" CONNECT TO PI AND CREATE LED BOARD OBJECT """
# Select file and create connection object
# Open conf file (read json for IP and connect)
conf_file = json_reader.JSONReads.reader(config_selector.ConfSelect.selection())  # use default file and open it

"""  Create config reader and connection objects"""
conf_reader = json_reader.JSONReads
pi_conn = connector.PiConnect.single_factory_connector(conf_reader.finder(conf_file, "connection", "ip_add"))

""" Get an LED board up and running """
# read LED values from conf
LED_pins = conf_reader.finder(conf_file, "LEDs")
# Set the board up
LED_board = led_conn.LED(data_handlers.HandleData.dict_to_value_list(LED_pins), pi_conn)
LED_board = LED_board.board()

""" COPY THE FILES """

for s, d in dirs.items():
        LED_board.value = (1, 0, 1, 0, 1)
        LED_board.blink()
        sync(Path(s), Path(d), "sync", verbose=False, exclude=(regex,))
TearDown.down(LED_board)
