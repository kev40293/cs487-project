import web


class login:
    render = web.template.render('templates/')
    def GET(self):
        return self.render.login()
    def POST(self):
        return self.render.login()
