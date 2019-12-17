from startup_classes import connector, json_reader, config_selector
from default_classes import data_handlers
from teardown.teardown import TearDown
from led import led_conn
from dirsync import sync
from pathlib import Path


""" CONNECT TO PI AND CREATE LED BOARD OBJECT """
# Select file and create connection object
# Open conf file (read json for IP and connect)
# TODO: FIX this
conf_file = json_reader.JSONReads.reader(config_selector.ConfSelect.selection())  # use default file and open it

"""  Create config reader """
conf_reader = json_reader.JSONReads

""" FILE SYNC CONFIG """
# regex for ignore files
regex = r".+\.(txt|log|git|jar)$"

""" COPY THE FILES """
for s, d in conf_reader.finder(conf_file, "dirs").items():
    """ try and connect - want to allow back to run even if pi conn fails """
    try:
        pi_conn = connector.PiConnect.single_factory_connector(conf_reader.finder(conf_file, "connection", "ip_add"))

        """ Get an LED board up and running """
        # read LED values from conf
        LED_pins = conf_reader.finder(conf_file, "LEDs")
        # Set the board up
        LED_board = led_conn.LED(data_handlers.HandleData.dict_to_value_list(LED_pins), pi_conn)
        LED_board = LED_board.board()
        LED_board.blink()
    except (IOError, OSError) as error:
        print(f"{error} occurred when connecting to PI")
    # run the sync process
    sync(Path(s), Path(d), "sync", verbose=False, exclude=(regex,))
    """ wrap cleanup in try just in case pi conn fails"""
    try:
        TearDown.down(LED_board)
    except Exception as ex:
        print(ex)
