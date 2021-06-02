from Database import db, PrimaryKey, Required, Set


class Tarif(db.Entity):
    id = PrimaryKey(int, auto=True)
    tarif_name = Required(str)
    anothet_minute = Required(int)
    home_minute = Required(int)
    sms = Required(int)
    internet = Required(str)
    speed_internet = Required(str)
    cost = Required(str)
    transition_number = Required(str,unique=True)
    changelog = Set("Changelog",cascade_delete=True)
