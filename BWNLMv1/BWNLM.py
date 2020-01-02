from modul import sql_connect as sql
from modul import room_input
sql_connection = sql.sql_con()
accept = 0



if __name__ == "__main__":
    question = 0
    while question == 0:
        print("""
        Выберите пункт меню:
        1- Удаление всех карт к указанному номеру.
        2- Сброс состояния указанного номера.
        3- DML запросы к базе данных BWNKM2_DB ручной ввод. (commit запрещен)
        4- Добавить определенную карту в черный список программы.
        любой другой символ - закрытие сессии и выход из программы

        Формат ввода гостиничных номеров:
        1-14, 2101-2131, 2201-2229
        """)
        quest = input("Введите Ваш запрос:")
        if quest == '1':
            while True:
                try:
                    sql_connection.start_connect()
                except ValueError as e:
                    print('Нет соединения', e)
                else:
                    print('Есть соединение')
                    break


            try:
                date = int(input("Введите гостиничный номер: "))
                date_db=room_input.room(date)
                date_list=[]
                date_list.append(date_db)
                sql_connection.card(date_list)
            except ValueError as e:
                print ('Не верный ввод данных, или данные отсутствуют в таблице', e)



        elif quest == '2':
            while True:
                try:
                    sql_connection.start_connect()
                except ValueError as e:
                    print('Нет соединения', e)
                else:
                    print('Есть соединение')
                    break

            try:
                date = input("Введите гостиничный номер: ")
                date_list=['',]
                date_list.append (date)
                sql_connection.room(date_list)
            except ValueError as e:
                print ('Не верный ввод данных, или данные отсутствуют в таблице', e)



        elif quest == '3':
            while True:
                try:
                    sql_connection.start_connect()
                except ValueError as e:
                    print('Нет соединения', e)
                else:
                    print('Есть соединение')
                    break
            try:
                sql_connection.DML(input("Введите DML запрос: "))
            except ValueError as e:
                print('SQL не может распознать Ваш запрос', e)

        elif quest == '4':
            while True:
                try:
                    sql_connection.start_connect()
                except ValueError as e:
                    print('Нет соединения', e)
                else:
                    print('Есть соединение')
                    break

            try:
                date = input("Введите номер карты: ")
                date_list=['',]
                date_list.append (date)
                sql_connection.black_card(date_list)
            except ValueError as e:
                print ('Не верный ввод данных, или данные отсутствуют в таблице', e)



        else:
            break
