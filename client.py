class Client:
    """ Třída pro vytvoření nových pojištěných (instancí) """

    def __init__(self, first_name, last_name, age, email, phone, street, city, post_code):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.phone = phone
        self.street = street
        self.city = city
        self.post_code = post_code
    def __str__(self):
        return (f"{self.first_name}\t{self.last_name}\t{self.age}\t{self.phone}")
