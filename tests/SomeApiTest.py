import pytest

from rest.command.ApiService import ApiService
from rest.command.PostRequest import PostRequest
from rest.command.composite.PostCreator import PostCreator
from rest.command.composite.UserCreator import UserCreator
from rest.command.model.PostModel import PostModel


class TestApi:


    def test_delete_with_deps(self):
        post_dir = PostCreator().create_random()
        post_dir.delete_with_dependencies()

    @pytest.fixture()
    def create_user(self):
        user_cr = UserCreator().create_random()
        yield user_cr
        post_id = self.create_post.response_json['id']
        PostCreator().delete_by_id(post_id)

    def test_create_post(self, create_user):
        user_cr = create_user
        self.model = PostModel.random_values(userid=user_cr.id)
        self.create_post = PostRequest(ApiService(),
                                       ApiService.POSTS,
                                       self.model).execute()
