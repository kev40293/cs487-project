import web
from web import form

render = web.template.render("templates")

class login:
    def GET(self):
        return render.login()

    def POST(self):
        upass = web.input(username=None)
        user_type = login_user(upass.username, user.password)
        return str(upass.username) + " tried to log in"

    def login_user(self, user, password):
        pass
