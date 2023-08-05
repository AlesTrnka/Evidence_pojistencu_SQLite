from evidence import Evidence
import os

evidence = Evidence()   # Instance třídy Evidence

def run_app():
    """
    Průvodce aplikací.
    """
    evidence.create_table()     # Vytvožení tabulky pro evidenci údajů o klientech
    while True:
        os.system('cls')
        print("Vítejte v aplikaci EVIDENCE POJIŠTĚNCŮ\n")
        evidence.operation_list()   # Vypíše seznam operací, které lze provést.
        choice = input("\nZadejte volbu:\t")
        if choice == "1":
            os.system('cls')
            print("Přidání nového klienta")
            print("ˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇ\n")
            first_name = input("Zadejte křestní jméno:\n").capitalize()
            last_name = input("Zadejte příjmení:\n").capitalize()
            age = input("Zadejte věk:\n")
            email = input("Zadejte e-mail:\n")
            phone = input("Zadejte telefonní číslo:\n")
            street = input("Zadejte ulici bydliště a číslo popisné:\n")
            city = input("Zadejte město bydliště\n").capitalize()
            post_code = input("Zadejte poštovní směrovací číslo:\n")
            evidence.add_client(first_name, last_name, age, email, phone, street, city, post_code)  # Přidání klienta do databáze.
            print("\nPojištěnec byl zaevidován do databáze.")
            input("Pokračujte klávesou Enter. . .")
        elif choice == "2":
            os.system('cls')
            print("Výpis pojištěnců z databáze (limit - 50):\n")
            print("ID / Jméno / Příjmení , Věk:")
            evidence.view_clients() # Zobrazí seznam klientů v databázi.
            input("\nPokračujte klávesou Enter. . .")
        elif choice == "3":
            os.system('cls')
            print(f"VYHLEDÁNÍ POJIŠTĚNÉHO")
            print("ˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇ\n")
            first_name = input("Zadejte křestní jméno:\n").capitalize()
            last_name = input("Zadejte příjmení:\n").capitalize()
            os.system('cls')
            print(f"Pro zadané jméno {first_name} {last_name} jsou nalezeny tyto záznamy:\n")
            print("\nID / Jméno / Příjmení , Věk / Email, Telefon, Ulice a ČP, Město, PSČ")
            print("ˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇ")
            evidence.find(first_name, last_name)     # Vyhledá klienta a zobrazí údaje.
            input("\nPokračujte klávesou Enter. . .")
        elif choice == "4":
            os.system('cls')
            print(f"EDITACE POJIŠTĚNÉHO")
            print("ˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇˇ\n")
            first_name = input("Zadejte jméno člověka, kterého chcete editovat:\n").capitalize()
            last_name = input("Zadejte příjmení člověka, kterého chcete editovat:\n").capitalize()
            var_dict = {"jméno":"first_name", "příjmení":"last_name", "věk":"age", "email":"email", "telefon":"phone", "ulice_čp":"street", "město":"city", "psč":"post_code"}
            variable = input("Který údaj chcete aktualizovat? (jméno, příjmení, věk, email, telefon, ulice_ČP, město, PSČ)\n").lower()
            value = input("Napište novou hodnotu:\t")
            evidence.edit(first_name, last_name, var_dict[variable], value) # Editace údajů o klientovi.
            print("Pojištěnec má nyní v databázi tyto údaje :\n")
            print("\nID / Jméno / Příjmení , Věk / Email, Telefon, Ulice a ČP, Město, PSČ")
            evidence.find(first_name, last_name)    # Vyhledá klienta a zobrazí údaje.
            input("\nPokračujte klávesou Enter. . .")
        elif choice == "5":
            os.system('cls')
            print("Přeji hezký den.")
            input("\nUkončete klávesou Enter. . .")
            return False    # Ukončí aplikaci
        else:
            print("Neplatné zadání, zvolte mezi čísly 1 až 5.")
            input("\nPokračujte klávesou Enter. . .")


