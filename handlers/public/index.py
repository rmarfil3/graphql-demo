from handlers.public.base import BaseHandler


class IndexPage(BaseHandler):
    def get(self):
        self.render_template("templates/index.html")
