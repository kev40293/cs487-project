import web
import bcrypt

render = web.template.render("templates")

class login:
    def GET(self):
        return render.login()

    def POST(self):
        upass = web.input(username=None)
        user_type = login_user(upass.username, user.password)
        if user_type == None:
            return "Username or password not valid"
        return str(upass.username) + " logged in as " + user_type

    def login_user(self, user, password):
        user_data = self.get_user(user)
        if (user_data == None):
            return None
        elif (user_data.passhash == bcrypt.hashpw(password, user_data.passhash)):
            return user_data.utype
        else:
            return None

    def get_user(self,user):
        return None
