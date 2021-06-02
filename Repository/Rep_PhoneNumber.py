from pony.orm import db_session, commit

from Entites.en_base import PhoneNumber


class PhoneNumberRepository:
    def __init__(self):
        pass

    def get_dict(self) -> dict:
        return self.p_dict

    def set_dict(self, p_dict: dict) -> None:
        self.p_dict = p_dict

    @db_session
    def get_phonenumbers(self) -> list:
        return list(map(lambda item: item.to_dict(), PhoneNumber.select()[:]))

    @db_session
    def del_phonenumber(self, phn_d: dict) -> None:
        phn = PhoneNumber.select(lambda c: c.id == phn_d['id'])
        phn.delete()

    @db_session
    def new_phonenumber(self, phn_d: dict) -> int:
        new_phn = PhoneNumber(phone_number=phn_d['phone_number'])
        commit()
        return new_phn.id

    @db_session
    def update_phonenumber(self, phn_d: dict) -> None:
        phn = PhoneNumber[phn_d['id']]
        phn.phone_number = phn_d['phone_number']

    @db_session
    def get_phonenumber(self, phn_d: dict) -> dict:
        phn = PhoneNumber.get(phone_number=phn_d['phone_number'])
        phn_d = {'id': phn.id, 'phone_number': phn.phone_number}
        return phn_d
