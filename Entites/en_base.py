from pony.orm import db_session, sql_debug

from Database import db
from Entites.en_Abonent import Abonent
from Entites.en_Address import Address
from Entites.en_Changelog import Changelog
from Entites.en_City import City
from Entites.en_Contract import Contract
from Entites.en_Passport import Passport
from Entites.en_PhoneNumber import PhoneNumber
from Entites.en_SimCard import SimCard
from Entites.en_Tarif import Tarif

sql_debug(True)
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
'''
with db_session:
    pas1 = Passport(serial="1375", number="450644")
    pas2 = Passport(serial="1375", number="456055")
    pas3 = Passport(serial="1375", number="457055")
    pas4 = Passport(serial="1375", number="459085")
    cit1 = City(city_name="Самара")
    cit2 = City(city_name="Новосибирск")
    cit3 = City(city_name="Пермь")
    cit4 = City(city_name="Красноярск")
    Adr1 = Address(street="Южная", home="23", city=cit1)
    Adr2 = Address(street="Западная", home="32", city=cit2)
    Adr3 = Address(street="Северная", home="10", city=cit3)
    Adr4 = Address(street="Восточная", home="51", city=cit4)
    Abo1 = Abonent(last_name="Ткачёв", first_name="Алексей", patronymic="Дмитреевич", age=25, passport=pas1,
                   address=Adr1)
    Abo2 = Abonent(last_name="Порейкин", first_name="Евгений", patronymic="Васильевич", age=27, passport=pas2,
                   address=Adr2)
    Abo3 = Abonent(last_name="Смолин", first_name="Денис", patronymic="Сергеевич", age=30, passport=pas3, address=Adr3)
    Abo4 = Abonent(last_name="Вшивков", first_name="Игорь", patronymic="Константинович", age=35, passport=pas4,
                   address=Adr4)
    Sim1 = SimCard(ICCIM=1111111)
    Sim2 = SimCard(ICCIM=2222222)
    Sim3 = SimCard(ICCIM=3333333)
    Sim4 = SimCard(ICCIM=4444444)
    Con1 = Contract(date="21.06.2000", number_contract=1, number_abonent=5, simcard=Sim1, abonent=Abo1)
    Con2 = Contract(date="10.12.2003", number_contract=2, number_abonent=6, simcard=Sim2, abonent=Abo2)
    Con3 = Contract(date="15.11.2003", number_contract=3, number_abonent=7, simcard=Sim3, abonent=Abo3)
    Con4 = Contract(date="29.03.2003", number_contract=4, number_abonent=8, simcard=Sim4, abonent=Abo4)

    Phn1 = PhoneNumber(phone_number="79058564309", simcard=Sim1)
    Phn2 = PhoneNumber(phone_number="79091552954", simcard=Sim2)
    Phn3 = PhoneNumber(phone_number="79091552958", simcard=Sim3)
    Phn4 = PhoneNumber(phone_number="79091552959", simcard=Sim4)
    Tar1 = Tarif(tarif_name="Начальный",anothet_minute=100, home_minute=75, sms=500, internet="10ГБ",
                 speed_internet="20/40",cost="200 руб/м", transition_number="*630*1#")
    Tar2 = Tarif(tarif_name="Домашний",anothet_minute=250, home_minute=225, sms=500, internet="15ГБ",
                 speed_internet="30/100",cost="380 руб/м", transition_number="*626*1#")
    Tar3 = Tarif(tarif_name="Продвинутый",anothet_minute=300, home_minute=275, sms=500, internet="20ГБ",
                 speed_internet="50/150",cost="500 руб/м", transition_number="*620*1#")

    Cng1 = Changelog(data_change="28.09.2003", content="Изменена стоимость тарифа ", tarif=Tar1)
    Cng2 = Changelog(data_change="31.03.2004", content="Изменём номер телефона для перехода на тариф", tarif=Tar2)
    Cng3 = Changelog(data_change="17.03.2004", content="Изменена стоимость тарифа", tarif=Tar2)
    Cng4 = Changelog(data_change="10.05.2005", content="Изменём номер телефона для перехода на тариф", tarif=Tar3)'''
