from datetime import timedelta, datetime


class Document:
    def __init__(self, identifier, first_name, surname, issue_date):
        self.identifier = identifier
        self.first_name = first_name
        self.surname = surname
        self.issue_date = issue_date


class Passport(Document):
    def __init__(self, identifier, first_name, surname, place_of_birth, date_of_birth, issue_date):
        super().__init__(identifier, first_name, surname, issue_date)
        self.place_of_birth = place_of_birth
        self.date_of_birth = date_of_birth
        self.expiration = issue_date + timedelta(weeks=520)

    def is_valid_today(self):
        return datetime.now() >= self.date_of_birth

    def __str__(self):
        return self.identifier + "-" + self.first_name + " " + self.surname


my_passport = Passport("abcdef", "John", "Doe", "Sao Carlos - SP", datetime(1994, 1, 1), datetime(2021, 1, 1))
print(my_passport.first_name)
print(my_passport.expiration)
print(my_passport.is_valid_today())
print(my_passport)
