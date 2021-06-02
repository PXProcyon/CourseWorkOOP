from pony.orm import db_session, commit

from Entites.en_base import Contract


class ContractRepository:
    def __init__(self):
        pass

    def get_dict(self) -> dict:
        return self.p_dict

    def set_dict(self, p_dict: dict) -> None:
        self.p_dict = p_dict

    @db_session
    def get_contracts(self) -> list:
        return list(map(lambda item: item.to_dict(), Contract.select()[:]))

    @db_session
    def del_contract(self, cont_d: dict) -> None:
        cont = Contract.select(lambda c: c.id == cont_d['id'])
        cont.delete()

    @db_session
    def new_contract(self, cont_d: dict) -> int:
        new_cont = Contract(date=cont_d['date'], number_contract=cont_d['number_contract'],
                            number_abonent=cont_d['number_abonent'])
        commit()
        return new_cont.id

    @db_session
    def update_contract(self, cont_d: dict) -> None:
        cont = Contract[cont_d['id']]
        cont.date = cont_d['date']
        cont.number_contract = cont_d['number_contract']
        cont.number_abonent = cont_d['number_abonent']

    @db_session
    def get_contract(self, cont_d: dict) -> dict:
        cont = Contract.get(date=cont_d['date'], number_contract=cont_d['number_contract'],
                            number_abonent=cont_d['number_abonent'])
        cont_d = {'id': cont.id, 'date': cont.date, 'number_contract': cont.number_contract,
                  'number_abonent': cont.number_abonent}
        return cont_d
