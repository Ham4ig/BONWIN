import pypyodbc
class sql_con(object):
    """docstring for sql_con."""
    DSN = 'DSN=BWNLM'
    db = 'DATABASE=BWNLM2_DB'
    user = "UID="
    pw = "PWD="
    conn = ''
    cursor = ''



    def start_connect(self):
        self.user = ("UID="+input('логин= '))
        self.pw =  ("PWD="+input("Пароль = "))
        conn_str = ';'.join([self.DSN, self.db, self.user, self.pw])
        print(conn_str)
        try:
            self.conn = pypyodbc.connect(conn_str)
            self.cursor = self.conn.cursor()
        except pypyodbc.Error as e:
            raise ValueError ("Неверные данные", e)

    def DML (self, inp):
        try:
            self.cursor.execute(inp)
            print(self.cursor.fetchall())
        except pypyodbc.ProgrammingError as e:
            self.cursor.close()
            self.conn.close()
            raise ValueError ("Не верный запрос в SQL QUERRY", e)

    def card (self, inp):
        try:
            self.cursor.execute('DELETE from dbo.CARDINFO where C_ROOMNO = ?;',(inp))
        except pypyodbc.ProgrammingError as e:
            self.cursor.close()
            self.conn.close()
            raise ValueError ("ошибка ввода данных", e)
        else:
            self.cursor.commit()
            self.cursor.close()
            self.conn.close()

    def room (self, inp):

        try:
            self.cursor.execute('UPDATE dbo.ROOMLIST SET I_USEBED = 0,I_STATE = 0, C_KNAME = ? WHERE C_ROOMNO = ?;',(inp))
        except pypyodbc.ProgrammingError as e:
            self.cursor.close()
            self.conn.close()
            raise ValueError ("ошибка ввода данных", e)
        else:
            self.cursor.commit()
            self.cursor.close()
            self.conn.close()

    def black_card (self, inp):
        try:
            self.cursor.execute('UPDATE dbo.CARDINFO SET C_ROOMNO = 00000000 WHERE C_CARDID = ?;',(inp))
        except pypyodbc.ProgrammingError as e:
            self.cursor.close()
            self.conn.close()
            raise ValueError ("ошибка ввода данных", e)
        else:
            self.cursor.commit()
            self.cursor.close()
            self.conn.close()
