#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import tornado.ioloop
import tornado.web
import sqlite3

import json


def _execute(query):
    dbPath = 'data.db'
    connection = sqlite3.connect(dbPath)
    cursorobj = connection.cursor()
    try:
        cursorobj.execute(query)
        result = cursorobj.fetchall()
        connection.commit()
    except Exception:
        raise
    connection.close()
    return result


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        rows = _execute('SELECT * FROM test')
        data_list = []
        for row in rows:
            data_list.append(row)
        self.write(json.dumps(data_list))

application = tornado.web.Application([
    (r"/", MainHandler),
    ],
    template_path=os.path.join(os.getcwd(), "templates"),
    static_path=os.path.join(os.getcwd(), "static"),
    )


if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


# End of Line.
