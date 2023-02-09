import string
import random
import datetime


class DataGenerator:
    def __init__(self):
        self.chars_all = (
                string.ascii_letters
                + string.digits
                + string.punctuation
                + string.whitespace
        )
        self.chars_no_whitespace = (
                string.ascii_letters + string.digits + string.punctuation
        )
        self.chars_letters_and_digits = string.ascii_letters + string.digits
        self.username_length = random.randint(5, 15)
        self.password_length = random.randint(5, 15)
        self.names = [
            "Amelia",
            "Anna",
            "Anthony",
            "Emma",
            "Ethan",
            "Lucas",
            "Luna",
            "Oliver",
            "Olivia",
            "Samuel",
            "Sophia",
            "Stevie",
            "Taylor",
            "Valery",
            "Victoria",
        ]

    def generate_username(self, username_length=None):
        if not username_length:
            username_length = self.username_length

        return "".join(
            random.choice(self.chars_letters_and_digits) for _ in range(username_length)
        )

    def generate_password(self, password_length=None):
        if not password_length:
            password_length = self.password_length
        return "".join(
            random.choice(self.chars_no_whitespace) for _ in range(password_length)
        )

    def generate_correct_name(self):
        return random.choice(self.names)

    def generate_incorrect_name(self):
        return "".join(
            random.choice(self.chars_all) for _ in range(self.username_length)
        )

    def generate_random_email(self):
        email = random.choice(self.names) + ''.join("@gmail.com")
        return str(email)

    def different_password(self):
        password = "987654321"
        return password

    def generate_random_pesel(self):
        digits = "123456789"
        digits_with_zero = digits + "0"

        number = random.choice(digits) + ''.join(random.choice(digits_with_zero) for _ in range(10))
        return str(number)

    def generate_random_date(self):
        start_date = datetime.date(1970, 1, 1)
        end_date = datetime.date(2005, 2, 1)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        return str(random_date)

    def password(self):
        password = "123456789"
        return password
