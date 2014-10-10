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
web.config._session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'loggedin' : False, 'role': None})

def render_page(content):
    session = web.config._session
    banner = render.banner(session.loggedin)
    page = None
    return render.base(session.role, banner, page)

class index():
    def GET(self):
        return render_page(None)

if __name__ == "__main__":
    app.run()
