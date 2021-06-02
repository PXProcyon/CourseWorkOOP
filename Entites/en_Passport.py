from Database import db, PrimaryKey, Required, composite_index, Optional


class Passport(db.Entity):
    id = PrimaryKey(int, auto=True)
    serial = Required(str)
    number = Required(str)
    abonent = Optional("Abonent")
    composite_index(serial,number)