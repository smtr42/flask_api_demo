from flask import Blueprint
# from ems.communication.flask.app.blueprints.api.ems.graph import ems_graph_blueprint
from flask_restful import Api

from outer_folders.handlers.alarm_handler import AlarmsHandler
from outer_folders.handlers.graph_handler import GraphHandler



from ems.communication.flask.app.resource.generic_resource import GenericResource

handler_list = (AlarmsHandler, GraphHandler,)

def create_blueprint_and_register(blueprint_name: str,handler_class,parent_blueprint: Blueprint,api_url_preffix: str = "",api_endpoint: str = "",**kwargs): 
    """Create blueprint and register it to the app.
    TODO: write documentation
    """
    blueprint = Blueprint(blueprint_name, __name__, url_prefix=handler_class.LINK_URL)
    api = Api(blueprint)
    api.add_resource(
        GenericResource,
        api_url_preffix,
        endpoint=api_endpoint,
        resource_class_kwargs={"handler": handler_class},
    )
    parent_blueprint.register_blueprint(blueprint)
    return parent_blueprint

version_1_blueprint = Blueprint("version_1", __name__, url_prefix="")

for handler in handler_list:
    create_blueprint_and_register(
        handler.__name__,
        handler,
        version_1_blueprint,
    )