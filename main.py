#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import webapp2
from webapp2_extras import routes

# public
from handlers.public.index import IndexPage

app = webapp2.WSGIApplication([
    routes.DomainRoute(r'<:.*>', [
        webapp2.Route('/', handler=IndexPage, name="www-index")
    ])
])
