from pony.orm import db_session, commit

from Entites.en_base import Address


class AddressRepository:
    def __init__(self):
        pass

    def get_dict(self) -> dict:
        return self.p_dict

    def set_dict(self, p_dict: dict) -> None:
        self.p_dict = p_dict

    @db_session
    def get_addresss(self) -> list:
        return list(map(lambda item: item.to_dict(), Address.select()[:]))

    @db_session
    def del_address(self, addr_d: dict) -> None:
        addr = Address.select(lambda c: c.id == addr_d['id'])
        addr.delete()

    @db_session
    def new_address(self, addr_d: dict) -> int:
        new_addr = Address(street=addr_d['street'], home=addr_d['home'])
        commit()
        return new_addr.id

    @db_session
    def update_address(self, addr_d: dict) -> None:
        addr = Address[addr_d['id']]
        addr.street = addr_d['street']
        addr.home = addr_d['home']

    @db_session
    def get_address(self, addr_d: dict) -> dict:
        addr = Address.get(street=addr_d['street'], home=addr_d['home'])
        addr_d = {'id': addr.id, 'street': addr.street, 'home': addr.home}
        return addr_d
