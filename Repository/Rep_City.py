from pony.orm import db_session, commit

from Entites.en_base import City


class CityRepository:
    def __init__(self):
        pass

    def get_dict(self) -> dict:
        return self.p_dict

    def set_dict(self, p_dict: dict) -> None:
        self.p_dict = p_dict

    @db_session
    def get_citys(self) -> list:
        return list(map(lambda item: item.to_dict(), City.select()[:]))

    @db_session
    def del_city(self, city_d: dict) -> None:
        city = City.select(lambda c: c.id == city_d['id'])
        city.delete()

    @db_session
    def new_city(self, city_d: dict) -> int:
        new_cit = City(city_name=city_d['city_name'])
        commit()
        return new_cit.id

    @db_session
    def update_city(self, city_d: dict) -> None:
        cit = City[city_d['id']]
        cit.city_name = city_d['city_name']

    @db_session
    def get_city(self, city_d: dict) -> dict:
        cit = City.get(city_name=city_d['city_name'])
        cit_d = {'id': cit.id, 'city_name': cit.city_name}
        return cit_d
