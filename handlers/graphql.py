import ast
import logging
import traceback

from graphene.utils.str_converters import to_camel_case
from graphene_gae.webapp2 import GraphQLHandler

from base.handler import LogExceptionHandler, symphlogger, SYMPHMONITOR_API_KEY
from handlers import exceptions
from handlers.decorators import log_arguments
from handlers.exceptions import model_exceptions
from libraries.graphql import GraphQLError
from libraries.graphql.error import format_error
from models.accounts.account import Account
from schemas import accounts


class AccountsGraphQLHandler(GraphQLHandler):
    def _get_schema(self):
        return accounts.schema
