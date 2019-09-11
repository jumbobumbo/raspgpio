from startup_classes import connector, json_reader, config_selector
from led import led_conn

""" Select file and create connection object """
# Open conf file (read json for IP and connect)
conf_file = json_reader.JSONReads.reader(config_selector.ConfSelect.selection())  # use default file and open it
"""  Create config reader and connection objects"""
conf_reader = json_reader.JSONReads
pi_conn = connector.PiConnect.single_factory_connector(conf_reader.finder(conf_file, "connection", "ip_add"))

""" Get an LED board up and running """
# read LED values from conf
LED_pins = conf_reader.finder(conf_file, "LEDs")
print(LED_pins)
