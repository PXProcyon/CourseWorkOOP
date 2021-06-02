from Database import db, PrimaryKey, Required, Optional


class Address(db.Entity):
    id = PrimaryKey(int, auto=True)
    street = Required(str)
    home = Required(str)
    city = Optional("City")
    abonent = Optional("Abonent")