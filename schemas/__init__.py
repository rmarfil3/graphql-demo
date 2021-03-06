import graphene

import user


class Query(user.Query, graphene.ObjectType):
    # node = graphene.relay.Node.Field()
    pass


class Mutation(user.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
