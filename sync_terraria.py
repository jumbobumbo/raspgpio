from pathlib import Path
from default_classes.sync import LEDSyncer


LEDSyncer("pi_ip_add", "LEDs",
          r".+\.(txt|log|git|jar)$",
          "terraria",
          Path(str(Path.cwd()), "config/", "default_config.json")
          ).file_sync_LED()
