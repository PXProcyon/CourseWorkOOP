from pony.orm import db_session, commit

from Entites.en_base import Changelog


class ChangelogRepository:
    def __init__(self):
        pass

    def get_dict(self) -> dict:
        return self.p_dict

    def set_dict(self, p_dict: dict) -> None:
        self.p_dict = p_dict

    @db_session
    def get_changelogs(self) -> list:
        return list(map(lambda item: item.to_dict(), Changelog.select()[:]))

    @db_session
    def del_changelog(self, chang_d: dict) -> None:
        cng = Changelog.select(lambda c: c.id == chang_d['id'])
        cng.delete()

    @db_session
    def new_changelog(self, chang_d: dict) -> int:
        new_cng = Changelog(data_change=chang_d['data_change'], content=chang_d['content'])
        commit()
        return new_cng.id

    @db_session
    def update_changelog(self, chang_d: dict) -> None:
        cng = Changelog[chang_d['id']]
        cng.data_change = chang_d['data_change']
        cng.content = chang_d['content']

    @db_session
    def get_changelog(self, chang_d: dict) -> dict:
        cng = Changelog.get(data_change=chang_d['data_change'], content=chang_d[' content'])
        change_d = {'id': cng.id, 'data_change': cng.data_change, 'content': cng.content}
        return change_d