from Database import db, PrimaryKey, Required, Optional,Set


class Abonent(db.Entity):
    id = PrimaryKey(int, auto=True)
    first_name = Required(str)
    last_name = Required(str)
    patronymic = Optional(str)
    age = Required(int)
    passport = Optional("Passport", cascade_delete=True)
    address = Optional("Address", cascade_delete=True)
    contract = Set("Contract", cascade_delete=True)

