from pony.orm import db_session, commit

from Entites.en_base import Passport


class PassportRepository:
    def __init__(self):
        self.p_dict = {}

    def get_dict(self) -> dict:
        return self.p_dict

    def set_dict(self, p_dict: dict) -> None:
        self.p_dict = p_dict

    @db_session
    def get_passports(self) -> list:
        return list(map(lambda item: item.to_dict(), Passport.select()[:]))

    @db_session
    def del_passport(self, passport_d: dict) -> None:
        pas = Passport.select(lambda c: c.id == passport_d['id'])
        pas.delete()

    @db_session
    def new_passport(self, passport_d: dict) -> int:
        new_passport = Passport(serial=passport_d['serial'], number=passport_d['number'])
        commit()
        return new_passport.id

    @db_session
    def update_passport(self, passport_d: dict) -> None:
        pas = Passport[passport_d['id']]
        pas.serial = passport_d['serial']
        pas.number = passport_d['number']

    @db_session
    def get_passport(self, passport_d: dict) -> dict:
        pas = Passport.get(serial=passport_d['serial'], number=passport_d['number'])
        pas_d = {'id': pas.id, 'serial': pas.serial, 'number': pas.number}
        return pas_d
