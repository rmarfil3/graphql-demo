import graphene
from graphene_gae import NdbObjectType, NdbConnectionField

from models.user import User


# class UserType(NdbObjectType):
#     class Meta:
#         model = User
#         interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    # users = NdbConnectionField(UserType)
    #
    # def resolve_users(self, info, **kwargs):
    #     return User.query()

    x = graphene.String()

    def resolve_x(self, info, **kwargs):
        return "Hello"


# class Register(graphene.relay.ClientIDMutation):
#     class Input:
#         name = graphene.String()
#         email = graphene.String()
#
#     user = graphene.Field(UserType)
#
#     @classmethod
#     def mutate_and_get_payload(cls, root, info, name, email):
#         user = User()
#         user.name = name
#         user.email = email
#         user.put()
#
#         return Register(user=user)
#
#
# class Mutation(graphene.ObjectType):
#     register = Register.Field(description="Register a new user")
