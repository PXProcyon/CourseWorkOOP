from pony.orm import db_session, commit

from Entites.en_base import Tarif


class TarifRepository:
    def __init__(self):
        pass

    def get_dict(self) -> dict:
        return self.p_dict

    def set_dict(self, p_dict: dict) -> None:
        self.p_dict = p_dict

    @db_session
    def get_tarifs(self) -> list:
        return list(map(lambda item: item.to_dict(), Tarif.select()[:]))

    @db_session
    def del_tarif(self, tar_d: dict) -> None:
        tar = Tarif.select(lambda c: c.id == tar_d['id'])
        tar.delete()

    @db_session
    def new_tarif(self, tar_d: dict) -> int:
        new_tar = Tarif(tarif_name=tar_d['tarif_name'],
                        anothet_minute=tar_d['another_minute'],
                        home_minute=tar_d['home_minute'],
                        sms=tar_d['sms'], internet=tar_d['internet'],
                        speed_internet=tar_d['speed_internet'],
                        cost=tar_d['cost'], transition_number=tar_d['traslate_number'])
        commit()
        return new_tar.id

    @db_session
    def update_tarif(self, tar_d: dict) -> None:
        tar = Tarif[tar_d['id']]
        tar.tarif_name = tar_d['tarif_name']
        tar.anothet_minute = tar_d['anothet_minute']
        tar.home_minute = tar_d['home_minute']
        tar.sms = tar_d['sms']
        tar.internet = tar_d['internet']
        tar.speed_internet = tar_d['speed_internet']
        tar.cost = tar_d['cost']
        tar.transition_number = tar_d['transition_number']

    @db_session
    def get_tar(self, tar_d: dict) -> dict:
        tar = Tarif.get(tarif_name=tar_d['tarif_name'],
                        anothet_minute=tar_d['anothet_minute'],
                        home_minute=tar_d['home_minute'],
                        sms=tar_d['sms'], internet=tar_d['internet'],
                        speed_internet=tar_d['speed_internet'],
                        cost=tar_d['cost'], transition_number=tar_d['transition_number'])
        tar_d = {'id': tar.id, 'tarif_name': tar.tarif_name,
                 'anothet_minute': tar.anothet_minute,
                 'home_minute': tar.home_minute,
                 'sms': tar.sms, 'internet': tar.internet,
                 'speed_internet': tar.speed_internet, 'cost': tar.cost,
                 'transition_number': tar.transition_number}

        return tar_d
