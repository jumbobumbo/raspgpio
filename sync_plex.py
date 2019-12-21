from default_classes.sync import LEDSyncer
from startup_classes.config_selector import ConfSelect as conf

LEDSyncer("pi_ip_add", "LEDs",
          r".+\.(txt|log|git|jar)$",
          "plex",
          conf.selection()
          ).file_sync_LED()
