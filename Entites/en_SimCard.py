from Database import db, PrimaryKey, Required, Optional, Set


class SimCard(db.Entity):
    id = PrimaryKey(int, auto=True)
    ICCIM = Required(int,unique=True)
    contart = Optional("Contract")
    phoneNumber = Set("PhoneNumber")
