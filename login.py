import web
import bcrypt

class User():
    def __init__(self,n,p,t):
        self.uname = n
        self.passhash = p
        self.utype = t

class login:
    def POST(self):
        upass = web.input(username=None,password = None)
        user_type = self.login_user(upass.username.encode('UTF-8'), upass.password.encode('UTF-8'))
        if user_type == None:
            return "Username or password not valid"
        #return str(upass.username) + " logged in as " + user_type
        web.config._session.loggedin = True
        web.config._session.role = user_type
        raise web.seeother('/')

    def login_user(self, user, password):
        user_data = self.get_user(user)
        if (user_data == None):
            return None
        elif (str(user_data.passhash) == bcrypt.hashpw(password, str(user_data.passhash))):
            return user_data.utype
        else:
            return None

    def get_user(self,user):
        user = User("manager", "$2a$12$CyLyLDPA5NFTY48o3fANQOEsni38JgHBk3FNwdUFd1OwYMBZxN146", "manager")
        return user

class logout:
    def POST(self):
        web.config._session.loggedin = False
        raise web.seeother('/')
