from startup_classes import connector, json_reader, config_selector
from default_classes import data_handlers
from teardown.teardown import TearDown
from led import led_conn
import time

""" Select file and create connection object """
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
""" TESTING THE PINS"""
for i, v in enumerate(LED_board):
    LED_board.on(i)
    time.sleep(1)
# kill
TearDown.down(LED_board)
