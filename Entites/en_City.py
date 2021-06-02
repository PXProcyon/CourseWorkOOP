from Database import db, PrimaryKey, Required, Set


class City(db.Entity):
    id = PrimaryKey(int, auto=True)
    city_name = Required(str)
    address = Set("Address")

