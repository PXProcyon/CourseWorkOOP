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
from pony.orm import *

db.bind(provider='sqlite', filename='database.sqlite', create_db=False)
# set_sql_debug(True)

db.generate_mapping(create_tables=True)

with db_session:
    end = input(
        "1. Добавить абонента\n2. Изменить абонента\n3. Удалить абонента"
        "\n4. Добавить тариф\n5. Изменить тариф\n6. Удалить тариф\n7 Закончить сеанc\n")

    if end == "1":
        pas5 = Passport(serial=input("Введите серию паспорта абонента: "),
                        number=input("Введите номер паспорта абонента: "))
        cit5 = City(city_name=input("Введите город абонента: "))
        Adr5 = Address(street=input("Введите улицу абонента: "), home=input("Введите дом абонента: "), city=cit5)
        Abo5 = Abonent(last_name=input("Введите фамилию абонента: "), first_name=input("Введите имя абонента: "),
                       patronymic=input("Введите отчество абонента: "), age=int(input("Введите возраст абонента: ")),
                       passport=pas5, address=Adr5)
        Sim5 = SimCard(ICCIM=int(input("Введите номер ICCIM сим-карты: ")))
        Con5 = Contract(date=input("Введите дату контракта: "), number_contract=input("Введите номер контракта: "),
                        number_abonent=input("Введите номер абонента: "), simcard=Sim5, abonent=Abo5)
        Phn5 = PhoneNumber(phone_number=input("Введите номер телефона абонента: "), simcard=Sim5)
        commit()

    if end == "2":
        for abo in Abonent.select():
            print(abo.id, abo.last_name, abo.first_name)

        sel = int(input("Какого абонента вы хотите изменить? \n"))
        inp2 = input("1.Изменить пасспортные данные\n2.Изменить адресс абонента\n3.Изменить ФИО и возраст абонента\n"
                     "4.Изменить ICCIM Сим-карты\n5.Изменить номер телефона\n")

        if inp2 == "1":
            passport_change = Passport[sel]
            passport_change.set(serial=input("Изменение серии паспорта абонента: "),
                                number=input("Изменение серии паспорта абонента: "))

        elif inp2 == "2":
            address_change = Address[sel], City[sel]
            address_change.city_name = input("Изменение города абонента: ")
            address_change.street = input("Изменение улицы абонента: ")
            address_change.home = input("Изменение дома абонента: ")

        elif inp2 == "3":
            abonent_change = Abonent[sel]
            abonent_change.set(last_name=input("Изменение фамилии абонента: "), first_name=
            input("Изменение имени абонента: "), patronymic=input("Изменение отчества абонента: "), age=
                               int(input("Изменение возраста абонента: ")))

        elif inp2 == "4":
            SimCard[sel].ICCIM = input("Изменение ICCIM сим-карты абонента: ")

        elif inp2 == "5":
            PhoneNumber[sel].phone_number = input("Изменение номера телефона абонента: ")

    elif end == "3":
        for abo in Abonent.select():
            print(abo.id, abo.last_name, abo.first_name)

        sel = int(input("Какого абонента вы хотите удалить? \n"))
        Abonent.get(lambda p: p.id == sel).delete()


    elif end == "4":
        Tar5 = Tarif(tarif_name=input("Введите название тарифа: "),
                     anothet_minute=int(input("Введите кол-во минут на номера других операторов: ")),
                     home_minute=int(input("Введите кол-во минут на номера домащнего оператора: "))
                     , sms=int(input("Введите кол-во смс: "))
                     , internet=input("Введите кол-во интернет-соединения: "),
                     speed_internet=input("Введите скорость интернет-соединения: "),
                     cost=input("Введите стоимость тарифа: "),
                     transition_number=input("Введите номер перехода на тариф: "))
        Cng5 = Changelog(data_change=input("Введите дату изменения тарифа"), content=
        input("Введите содержимое текущего изменения тарифа: "), tarif=Tar5)

    elif end == "5":
        for tar in Tarif.select():
            print(tar.id, tar.tarif_name)

        sel = int(input("Какой тариф вы хотите изменить? \n"))

        tarif_change = Tarif[sel]
        tarif_change.set(tarif_name=input("Изменить название тарифа: "),
                         anothet_minute=int(input("Изменить кол-во минут на номера других операторов: ")),
                         home_minute=int(input("Изменить кол-во минут на номера домащнего оператора: "))
                         , sms=int(input("Изменить кол-во смс: "))
                         , internet=input("Изменить кол-во интернет-соединения: "),
                         speed_internet=input("Изменить скорость интернет-соединения: "),
                         cost=input("Изменить стоимость тарифа: "),
                         transition_number=input("Изменить номер перехода на тариф: "))

    elif end == "6":
        for tar in Tarif.select():
            print(tar.id, tar.tarif_name)

        sel = int(input("Какой тариф вы хотите удалить? \n"))
        Tarif.select(lambda p: p.id == sel).delete(bulk=True)

    elif end == "7":

        for abonent_view in Abonent.select():
            print(abonent_view.last_name, abonent_view.first_name, abonent_view.patronymic,
                  abonent_view.age)
            passport_view = abonent_view.passport
            if not passport_view:
                print("Отсуствует паспортные данные")
            else:
                print(passport_view.serial, passport_view.number)
            address_view = abonent_view.address
            if not address_view:
                print("Отсуствует адрес")
            else:
                print(address_view.street, address_view.home)
            for contract_view in abonent_view.contract:
                if not contract_view:
                    print("Отсуствует контракт с оператором")
                else:
                    print(contract_view.date,contract_view.number_contract, + contract_view.number_abonent)
            simcard_view = contract_view.simcard
            if not simcard_view:
                print("Отсуствует сим-карта")
            else:
                print(simcard_view.ICCIM)
            for phonenumber_view in simcard_view.phoneNumber:
                if not phonenumber_view:
                    print("Отсуствует номер телефона")
                else:
                    print(phonenumber_view.phone_number)
            changelog_view = phonenumber_view.changelog
            tarif_view = changelog_view.tarif
            if not tarif_view:
                print("Отсуствует тариф")
            else:
                print(tarif_view.tarif_name,tarif_view.anothet_minute,tarif_view.home_minute
                      ,tarif_view.sms,tarif_view.internet,
                 tarif_view.speed_internet,tarif_view.cost,tarif_view.transition_number)

