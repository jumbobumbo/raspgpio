# raspgpio sync
Some fun with a pi, GPIO and dirsync

This has changed from its initial conception, now focused purely on syncing with the fun on a pi involved.

sync_* py files in the root are to be used with the scheduler of your choice (cron, etc).
These allow for more focused sync intervals, without making my own scheduler (why god why?).

Config is read from json file.
includes:
  - ip of pi
  - led pin config of pi
  - dirs to sync
  
will require dirsync python package to run. check the pip files innit.
