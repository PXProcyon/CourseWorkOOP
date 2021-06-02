from Database import db, PrimaryKey, Required, Optional


class Contract(db.Entity):
    id = PrimaryKey(int, auto=True)
    date = Required(str)
    number_contract = Required(int,unique=True)
    number_abonent = Required(int,unique=True)
    abonent = Required("Abonent")
    simcard = Required("SimCard")


