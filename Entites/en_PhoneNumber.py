from Database import db, PrimaryKey, Required, Set, Optional


class PhoneNumber(db.Entity):
    id = PrimaryKey(int, auto=True)
    phone_number = Required(str, unique=True)
    simcard = Optional("SimCard")
    changelog = Set("Changelog")