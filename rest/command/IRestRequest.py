from abc import ABCMeta, abstractmethod
from autologging import logged
from rest.ApiClient import ApiService


@logged
class IRestRequest(metaclass=ABCMeta):
    api_service: ApiService

    def __init__(self, api_service, resource, model=None):
        self.response = None
        self.api_service = api_service
        self.resource = resource
        self.model = model

    @staticmethod
    @abstractmethod
    def execute(self):
        " A method each request should implement."

    def _parse(self, r):
        self.status_code = r.status_code
        self.__log.info('response: %s', r.text)
        self.response = r
        self.status_code = r.status_code
        if r.status_code not in [200, 201, 204]:
            raise APIException(f'Response code received {r.status_code} '
                               f',expected [200, 201, 204], '
                               f'{r.request.method} {r.url}, body: {r.text}')
        if r.text:
            try:
                self.response_json = r.json()
            except ValueError:
                raise APIException(
                    f'Cant convert response body to json {r.status_code} '
                    f'{r.request.method} {r.url}, body: {r.text}')


class APIException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
