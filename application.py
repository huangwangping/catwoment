#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# Copyright 2015
#
# @author: huangwangping
# Created Time: 2015-11-17
"""
"""
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.options import define, options

import settings
from routes import handlers

define("port", default=settings.port, help="run on the given port", type=int)
define("mysql", default=settings.mysql, help="mysql database host:port")


class Application(tornado.web.Application):
    def __init__(self):
        settings
        tornado.web.Application.__init__(self, handlers, [])

        self.conn = None  # mysql conn


def main():
    tornado.options.parse_command_line()
    server = tornado.httpserver.HTTPServer(Application())
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
