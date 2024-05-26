from dataclasses import dataclass

from faker import Faker


@dataclass
class PostModel:
    userid: int
    title: str
    body: str

    @staticmethod
    def random_values(userid=1):
        fk = Faker()
        return PostModel(userid=userid, title=fk.text(max_nb_chars=30),
                  body=fk.text(max_nb_chars=100))
