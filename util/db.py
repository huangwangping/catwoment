#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# Copyright 2015
#
# @author: huangwangping
# Created Time: 2015-11-18
"""
"""
import cymysql


class MysqlHelper:

    def __init__(self, host="localhost", port=3306, user=None, passwd="",
                 db=None, chartset="utf8"):
        """
        constructor, create a new mysql connect with configuration
        """
        try:
            self._conn = cymysql.Connect(host=host,
                                         port=port,
                                         user=user,
                                         passwd=passwd,
                                         db=db,
                                         chartset=chartset)
        except
