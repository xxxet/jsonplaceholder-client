from autologging import logged

from rest.command.IRestRequest import IRestRequest


@logged
class GetListRequest(IRestRequest):

    def __init__(self, service, resource):
        super().__init__(service, resource)

    def execute(self):
        self._parse(self.api_service.get(self.resource))
        return self
