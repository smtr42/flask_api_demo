from outer_folders.handlers.generic_handler import GenericHandler
from outer_folders.controllers.alarm_controller import AlarmController

class AlarmsHandler(GenericHandler):
    """Handler dispatching """

    LINK_URL = "/api/alarms"

    def get(self, args):
        """TODO."""
        return AlarmController.get_alarms(args)

    def delete(self, args):
        """TODO."""
        return AlarmController.delete_alarms(args)