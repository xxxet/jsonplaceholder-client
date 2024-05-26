from abc import ABCMeta, abstractmethod
from typing import List

from rest.ApiClient import ApiService
from rest.command.IRestRequest import IRestRequest


class ICreator(metaclass=ABCMeta):

    def __init__(self):
        self.dependencies: List['__class__'] = []
        self.apiService = ApiService()
        self.last_request: IRestRequest
        self.model = None
        self.id: int

    def _add_dependency(self, dep):
        self.dependencies.append(dep)

    @staticmethod
    @abstractmethod
    def create_random(self):
        """A method each creator should implement. Creates obj with random values"""

    @staticmethod
    @abstractmethod
    def delete(self):
        """ A method each Creator should implement. Deletes current obj."""

    def delete_with_dependencies(self):
        for dep in self.dependencies:
            dep.delete_with_dependencies()
