#!/usr/bin/python2
import web

from login import login

urls = (
        '/', 'index',
        '/login', 'login'
        )

class index():
    def GET(self):
        return "hello world"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
