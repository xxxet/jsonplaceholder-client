import requests
from autologging import logged


@logged
class ApiService:
    BASE_URL = 'https://jsonplaceholder.typicode.com'
    POSTS = 'posts'
    COMMENTS = 'comments'
    ALBUMS = 'albums'
    PHOTOS = 'photos'
    TODOS = 'todos'
    USERS = 'users'

    def __init__(self, ):
        self.response = None
        self.params = None
        self.cookies = None
        self.headers = None
        self.verify_https = True

    def delete(self, resource, obj_id):
        self.__log.info('delete(): %s, id: %s', resource, obj_id)
        return requests.delete(
            f'{self.BASE_URL}/{resource}/{obj_id}',
            headers=self.headers,
            cookies=self.cookies,
            verify=self.verify_https)

    def post(self, resource, json):
        self.__log.info('post() %s, json: %s', resource, json)
        return requests.post(f'{self.BASE_URL}/{resource}',
                             headers=self.headers,
                             cookies=self.cookies,
                             verify=self.verify_https,
                             json=json)

    def get(self, resource, params=None):
        self.__log.info('get(): %s, params: %s', resource, params)
        return requests.get(f'{self.BASE_URL}/{resource}',
                            params=params,
                            headers=self.headers,
                            cookies=self.cookies,
                            verify=self.verify_https, )

    def put(self, resource, json, obj_id):
        self.__log.info('put(): %s, json: %s', resource, json)
        return requests.put(
            f'{self.BASE_URL}/{resource}/{obj_id}',
            headers=self.headers,
            cookies=self.cookies,
            verify=self.verify_https,
            json=json)
