from Database import db, PrimaryKey, Required, Set, Optional


class Changelog(db.Entity):
    id = PrimaryKey(int, auto=True)
    data_change = Required(str)
    content = Required(str)
    phoneNumber = Set("PhoneNumber")
    tarif = Optional("Tarif")