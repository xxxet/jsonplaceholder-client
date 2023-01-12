from autologging import logged

from rest.command.IRestRequest import IRestRequest


@logged
class DeleteRequest(IRestRequest):
    def __init__(self, service, resource, obj_id):
        super().__init__(service, resource, None)
        self.obj_id = obj_id

    def execute(self):
        self._parse(self.api_service.delete(self.resource, self.obj_id))
        return self
