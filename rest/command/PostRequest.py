import dataclasses

from autologging import logged

from rest.command.IRestRequest import IRestRequest


@logged
class PostRequest(IRestRequest):
    def __init__(self, service, resource, model):
        super().__init__(service, resource, model)

    def execute(self):
        self._parse(self.api_service.post(self.resource,
                                          dataclasses.asdict(self.model)))
        return self
