# THUNetAutoLogin

Network autologin script for Tsinghua University which can keep your server online all the time. This script will login your acount in your server automatically, avoid the server being loged out when the link number reach maximun or due to other reasons.

## How to use
1. Set the `USERNAME` and `PASSWORD` in the line [5-6] of the `autologin.py` to your own acount setting.

2. Simply run the code below in the code directory.
```
python add_crontab.py
```

3. The script will auto run automatically each 15 minutes.

If your want to change the frequency, you can edit the `crontab_entry` variable in the line 6 of the `add_crontab.py` by yourself according to the crontab format. Or simply change 15 to any number you want that less than 60.

## Requirements

* Python 2.7
* Cron, and need your user has the privilege to use the cron on the server

