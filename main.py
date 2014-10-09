#!/usr/bin/python2
import web

from login import login, logout
from web import form

web.config.debug = False

urls = (
        '/', 'index',
        '/login', 'login',
        '/logout', 'logout'
        )
render = web.template.render("templates")
app = web.application(urls, globals())
web.config._session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'loggedin' : False})

class index():
    def GET(self):
        # Check if logged in
        session = web.config._session
        banner = render.banner(session.loggedin)
        page = None
        return render.base(session.role, banner, page)

if __name__ == "__main__":
    app.run()
