#!/usr/bin/python2
import web

from login import login

urls = (
        '/', 'index',
        '/login', 'login'
        )
render = web.template.render("templates")

class index():
    def GET(self):
        # Check if logged in
        # If not logged in
        return render.login()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
