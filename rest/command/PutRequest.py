import dataclasses

import requests
from autologging import logged

from rest.command.IRestRequest import IRestRequest


@logged

class PutRequest(IRestRequest):
    def execute(self):
        self._parse(self.api_service.put(self.resource,
                                         dataclasses.asdict(self.model)))
        return self
