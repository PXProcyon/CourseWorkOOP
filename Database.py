from pony.orm import *

db = Database()


class MyEntity(db.Entity):
    attr1 = Required(str)


session = db_session
