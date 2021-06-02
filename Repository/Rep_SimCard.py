from pony.orm import db_session, commit

from Entites.en_base import SimCard


class SimCardRepository:
    def __init__(self):
        pass

    def get_dict(self) -> dict:
        return self.p_dict

    def set_dict(self, p_dict: dict) -> None:
        self.p_dict = p_dict

    @db_session
    def get_simcards(self) -> list:
        return list(map(lambda item: item.to_dict(), SimCard.select()[:]))

    @db_session
    def del_simcard(self, sim_d: dict) -> None:
        sim = SimCard.select(lambda c: c.id == sim_d['id'])
        sim.delete()

    @db_session
    def new_simcard(self, sim_d: dict) -> int:
        new_sim = SimCard(ICCIM=sim_d['ICCIM'])
        commit()
        return new_sim.id

    @db_session
    def update_simcard(self, sim_d: dict) -> None:
        sim = SimCard[sim_d['id']]
        sim.date = sim_d['ICCIM']


    @db_session
    def get_simcard(self, sim_d: dict) -> dict:
        sim = SimCard.get(ICCIM=sim_d['ICCIM'])
        sim_d = {'id': sim.id, 'ICCIM': sim.date}
        return sim_d