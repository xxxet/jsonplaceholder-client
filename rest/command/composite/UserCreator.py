from rest.command.ApiService import ApiService
from rest.command.DeleteRequest import DeleteRequest
from rest.command.PostRequest import PostRequest
from rest.command.composite.ICreator import ICreator
from rest.command.model.UserModel import UserModel


class UserCreator(ICreator):

    def create_random(self):
        self.model = UserModel.random_values()
        create_user = PostRequest(self.apiService,
                                  ApiService.USERS,
                                  self.model).execute()
        self.id = create_user.response_json['id']
        return self

    def delete(self):
        DeleteRequest(self.apiService,
                      ApiService.USERS,
                      self.id).execute()

    def delete_with_dependencies(self):
        self.delete()