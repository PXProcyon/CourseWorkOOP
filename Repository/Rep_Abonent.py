from pony.orm import db_session, commit

from Entites.en_base import Abonent


class AbonentRepository:
    def __init__(self):
        pass

    def get_dict(self) -> dict:
        return self.p_dict

    def set_dict(self, p_dict: dict) -> None:
        self.p_dict = p_dict

    @db_session
    def get_abonents(self) -> list:
        return list(map(lambda item: item.to_dict(), Abonent.select()[:]))

    @db_session
    def del_abonent(self, abon_d: dict) -> None:
        abon = Abonent.select(lambda c: c.id == abon_d['id'])
        abon.delete()

    @db_session
    def new_abonent(self, abon_d: dict) -> int:
        new_abo = Abonent(last_name=abon_d['last_name'], first_name=abon_d['first_name'],
                          patronymic=abon_d['patronymic'], age=abon_d['age'])
        commit()
        return new_abo.id

    @db_session
    def update_abonent(self, abon_d: dict) -> None:
        abon = Abonent[abon_d['id']]
        abon.last_name = abon_d['last_name']
        abon.first_name = abon_d['first_name']
        abon.patronymic = abon_d['patronymic']
        abon.age = abon_d['age']

    @db_session
    def get_abonent(self, abon_d: dict) -> dict:
        abon = Abonent.get(last_name=abon_d['last_name'], first_name=abon_d['first_name'],
                           patronymic=abon_d['patronymic'], age=abon_d['age'])
        abon_d = {'id': abon.id, 'last_name': abon.last_name, 'first_name': abon.first_name,
                  'patronymic': abon.patronymic, 'age': abon.age}
        return abon_d
