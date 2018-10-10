from graphene_gae.webapp2 import GraphQLHandler

import schemas


class MyGraphQLHandler(GraphQLHandler):
    def _get_schema(self):
        return schemas.schema
