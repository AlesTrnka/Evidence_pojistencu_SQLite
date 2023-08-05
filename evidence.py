import sqlite3
import os
from client import Client

class Evidence:
    """
    Třída zahrnující funkce pro evidenci a správu údajů nových a stávajících klientů.
    """
    def __init__(self, ):
        self.conn = sqlite3.connect('databaze.db')
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """
        Vytvoření databáze, pokud již neexistuje.
        """
        self.c.execute("""CREATE TABLE IF NOT EXISTS klienti (
                klient_id INTEGER PRIMARY KEY AUTOINCREMENT,
                jméno TEXT,
                příjmení TEXT,
                věk INTEGER,
                email TEXT,
                telefon INTEGER,
                ulice_ČP TEXT,
                město TEXT,
                PSČ TEXT)""")

    def operation_list(self):
        """
        Vypíše seznam operací, které uživatel může provést.
        """
        operation = ["Přidat nového pojištěného", "Vypsat seznam pojištěných", "Vyhledat pojištěného a zobrazit podrobnosti", "Editovat pojištěnce", "Ukončit program"]
        for i in range(len(operation)):
            print(f"{i+1} - {operation[i]}")

    def add_client(self, first_name, last_name, age, email, phone, street, city, post_code):
        """
        Přidání klienta do databáze (Vytvoření instance třídy Client a zaznamenání údajů o klientovi do SQLite databáze).
        """
        new_client = Client(first_name, last_name, age, email, phone, street, city, post_code)
        client_details = (new_client.first_name, new_client.last_name, new_client.age, new_client.email, new_client.phone, new_client.street, new_client.city, new_client.post_code)
        self.c.execute("""INSERT OR IGNORE INTO klienti (
                'jméno', 'příjmení', 'věk', 'email', 'telefon', 'ulice_ČP','město', 'PSČ')
                VALUES(?,?,?,?,?,?,?,?)""", client_details)
        self.conn.commit()

    def view_clients(self):
        """
        Zobrazení seznamu zaevidovaných klientů(Limit 50 klientů.
        """
        self.c.execute("SELECT klient_id, jméno, příjmení, věk FROM klienti LIMIT 50")
        clients = self.c.fetchall()
        for client in clients:
            print(client)

    def find(self, first_name, last_name):
        """
        Vyhledání klienta v databázi.
        """
        self.c.execute("SELECT * FROM klienti WHERE jméno=(?) AND příjmení=(?)", (first_name, last_name))
        for i in self.c.fetchall():
            print(i)

    def edit(self, first_name, last_name, variable, value):
        """
        Editace údajů klienta v databázi.
        """
        self.c.execute("UPDATE klienti SET {}=? WHERE jméno=? AND příjmení=?".format(variable), (value, first_name, last_name))
        self.conn.commit()
