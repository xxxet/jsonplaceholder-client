from autologging import logged

from rest.command.IRestRequest import IRestRequest


@logged
class GetRequest(IRestRequest):

    def __init__(self, service, resource, obj_id):
        super().__init__(service, resource)
        self.obj_id = obj_id

    def execute(self):
        self._parse(self.api_service.get(f'{self.resource}/{self.obj_id}'))
        return self