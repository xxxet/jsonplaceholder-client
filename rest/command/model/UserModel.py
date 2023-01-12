from dataclasses import dataclass

from faker import Faker


@dataclass
class GeoModel:
    lat: str
    lng: str


@dataclass
class AddressModel:
    street: str
    suite: str
    city: str
    zipcode: str
    geo: GeoModel


@dataclass
class CompanyModel:
    name: str
    catchPhrase: str
    bs: str


@dataclass
class UserModel:
    name: str
    username: str
    email: str
    address: AddressModel
    phone: str
    website: str
    company: CompanyModel

    @staticmethod
    def random_values():
        fk = Faker()
        return UserModel(name=fk.name(),
                         username=fk.word() + fk.word().capitalize(),
                         email=fk.email(),
                         phone=fk.phone_number(),
                         website=f'http://{fk.word()}.com',
                         company=CompanyModel(name=fk.word(),
                                              catchPhrase=fk.text(max_nb_chars=100),
                                              bs=fk.word()),
                         address=AddressModel(street=fk.word(), suite=fk.word(),
                                              city=fk.city(), zipcode=fk.zipcode(),
                                              geo=GeoModel(lat=str(fk.latitude()),
                                                           lng=str(fk.longitude()))))