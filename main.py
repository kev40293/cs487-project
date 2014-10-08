#!/usr/bin/python2
import web

from login import login
web.config.debug = False

urls = (
        '/', 'index',
        '/login', 'login'
        )
render = web.template.render("templates")
app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'loggedin' : False})

class index():
    def GET(self):
        # Check if logged in
        if session.loggedin:
            return "You are logged in"
        # If not logged in
        else:
            return render.login()

if __name__ == "__main__":
    app.run()
