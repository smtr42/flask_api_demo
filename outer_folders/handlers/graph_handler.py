from outer_folders.handlers.generic_handler import GenericHandler
from outer_folders.controllers.graph_controller import GraphController

class GraphHandler(GenericHandler):
    """Handler dispatching """

    LINK_URL = "/api/graph"

    def get(self, args):
        """TODO."""
        return GraphController.get_graph(args)
