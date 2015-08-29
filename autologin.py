#!/usr/bin/env python
import urllib, urllib2, hashlib

LOGIN_URL = 'http://net.tsinghua.edu.cn/do_login.php'
USERNAME = 'USERNAME'  # Put your username here
PASSWORD = 'PASSWORD'  # Put your password here
AC_ID = '1'  # No idea what this param is use for

if __name__ == '__main__':
    auth_data = {
        'action': 'login',
        'username': USERNAME,
        'password': '{MD5_HEX}%s' % hashlib.md5(PASSWORD).hexdigest(),
        'ac_id': AC_ID
    }
    conn = urllib2.urlopen(LOGIN_URL, urllib.urlencode(auth_data))
    content = conn.read()
    if 'IP has been online, please logout.' not in content:
        print content
