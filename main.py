#!/usr/bin/env python
# -- coding: utf-8 --
import webapp2
from graphene_gae.webapp2 import GraphQLHandler
from webapp2_extras import routes

from handlers.graphql import MyGraphQLHandler
import schemas

config = {
    'graphql_schema': schemas.schema
}

app = webapp2.WSGIApplication([
    routes.DomainRoute(r'<:.*>', [
        # webapp2.Route('/graphql', handler=MyGraphQLHandler, name="www-graphql")
        webapp2.Route('/graphql', handler=GraphQLHandler, name="www-graphql")
    ]),
], config=config)
