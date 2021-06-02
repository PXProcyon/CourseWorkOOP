from Model.Abonent import Abonent
from Model.Changelog import Changelog
from Model.City import City
from Model.Contract import Contract
from Model.Passport import Passport
from Model.Adress import Address
from Model.PhoneNumber import PhoneNumber
from Model.SimCard import SimCard
from Model.Tarif import Tarif

pas1 = Passport("1375", "450644")
pas2 = Passport("1375", "456055")
cit1 = City("Самара")
cit2 = City("Новосибирск")
Adr1 = Address("Южная", "23", cit1)
Adr2 = Address("Западная", "32", cit2)
Abo1 = Abonent("Ткачёв", "Алексей", "Дмитреевич", 25, pas1, Adr1)
Abo2 = Abonent("Порейкин", "Евгений", "Васильевич", 27, pas2, Adr2)
Con1 = Contract("21.06.2000", 1, Abo1, 1,)
Con2 = Contract("10.12.2003", 2, Abo2, 2,)
Sim1 = SimCard(8970103, Con1)
Sim2 = SimCard(8071021, Con2)
Phn1 = PhoneNumber("79058564309", Sim1)
Phn2 = PhoneNumber("79091552954", Sim2)
Cng1 = Changelog("28.09.2003", "Изменена стоимость тарифа ", Phn1)
Cng2 = Changelog("31.03.2004", "Изменём номер телефона для перехода на тариф", Phn2)

Tar1 = Tarif(100, 75, 500, "10ГБ", "20/40", "200 руб/м", "*630*1#", Cng1)
Tar2 = Tarif(250, 225, 500, "15ГБ", "30/100", "380 руб/м", "*630*1#", Cng2)
print(Abo2,Adr2, Con2, Sim2, Phn2, sep='\n')


