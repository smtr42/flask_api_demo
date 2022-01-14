from flask_restful import Resource
from marshmallow import INCLUDE
from webargs.flaskparser import FlaskParser


class Parser(FlaskParser):
    """Custom parser used to pass unknown parameters to the handler."""

    DEFAULT_UNKNOWN_BY_LOCATION = {"query": INCLUDE}


parser = Parser()


class GenericResource(Resource):
    """
    Manage Handlers.
    """

    def __init__(self, *args, **kwargs) -> None:
        """Instanciate the right Handler wich will redirect the request"""
        self.handler = kwargs["handler"]()

    @parser.use_args({}, location="query")
    def get(self, args):
        """Generic get method redirecting to the good handler."""
        return self.handler.get(args), 200

    @parser.use_args({}, location="query")
    def post(self, args):
        return self.handler.post(args), 200

    @parser.use_args({}, location="query")
    def put(self, args):
        return self.handler.put(args), 200

    @parser.use_args({}, location="query")
    def delete(self, args):
        return self.handler.delete(args), 200