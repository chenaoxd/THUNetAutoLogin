#!/usr/bin/env python
import os, commands

if __name__ == '__main__':
    # The autologin crontab entry 
    crontab_entry = '*/15 * * * * %(current_dir)s/autologin.py >> %(current_dir)s/autologin.log 2>&1' \
                    % { 'current_dir': os.path.dirname(os.path.abspath(__file__)) }

    # Get current crontab status of the user
    crontab_existed, crontab_content = commands.getstatusoutput("crontab -l")

    if not crontab_existed:  # crontab existed
        if crontab_entry in crontab_content:  # already added
            print "Script already added to autorun list."
            
        elif crontab_content.strip():  # content empty
            autologin_crontab = open("./autologin.crontab", "w")
            autologin_crontab.write(crontab_content + '\n' + crontab_entry + '\n')
            autologin_crontab.flush()
            os.system("crontab ./autologin.crontab")
    else:  # crontab not existed
        os.system("echo '%s' > ./autologin.crontab" % crontab_entry)
        os.system("crontab ./autologin.crontab")
