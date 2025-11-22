class Person:
    def __init__(
        self,
        first_name,
        last_name,
        birth_date,
        job,
        working_years,
        salary,
        country,
        city,
        gender="unknown",
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.job = job
        self.working_years = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender

    def name(self):
        return f"{self.first_name} {self.last_name}"

    def age(self):
        day, month, year = map(int, self.birth_date.split("."))
        current_year = 2018
        current_month = 1
        current_day = 1

        age = current_year - year
        if (month, day) > (current_month, current_day):
            age -= 1
        return age

    def work(self):
        if self.gender == "male":
            return f"He is a {self.job}"
        elif self.gender == "female":
            return f"She is a {self.job}"
        else:
            return f"Is a {self.job}"

    def money(self):
        total = int(self.working_years * self.salary * 12)
        return f"{total:,}".replace(",", " ")

    def home(self):
        return f"Lives in {self.city}, {self.country}"
