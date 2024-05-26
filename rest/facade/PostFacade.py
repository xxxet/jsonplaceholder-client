from rest.ApiClient import ApiService
from rest.command.DeleteRequest import DeleteRequest
from rest.command.PostRequest import PostRequest
from rest.facade.ICreator import ICreator
from rest.facade.UserFacade import UserCreator
from rest.model.PostModel import PostModel


class PostCreator(ICreator):

    def create_random(self):
        user_cr = UserCreator()
        self._add_dependency(user_cr)
        user_cr.create_random()
        self.model = PostModel.random_values(userid=user_cr.id)
        create_post = PostRequest(self.apiService,
                                  ApiService.POSTS,
                                  self.model).execute()
        self.id = create_post.response_json['id']
        return self

    def delete_by_id(self, post_id):
        DeleteRequest(self.apiService,
                      ApiService.POSTS,
                      post_id).execute()

    def delete(self):
        DeleteRequest(self.apiService,
                      ApiService.POSTS,
                      self.id).execute()

    def delete_with_dependencies(self):
        DeleteRequest(self.apiService,
                      ApiService.POSTS,
                      self.id).execute()
        super().delete_with_dependencies()
