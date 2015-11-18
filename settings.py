#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# Copyright 2015
#
# @author: huangwangping
# Created Time: 2015-11-17
"""
"""
import os.path

port = 8000  # default port
mysql = "127.0.0.1:3306"  # default mysql
database = ""  # database
mysql_user = "root"  # db user
mysql_passwd = "root"  # db passwd
static_path = os.path.join(os.path.dirname(__file__), "../templates")
debug = True  # debug type
xsrf_cookies = True  #
cookie_secret = 'todo...'  #
