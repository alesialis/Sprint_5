import faker


def get_sign_up_data():
    fake = faker.Faker()
    name = fake.name()
    email = fake.email()
    password = fake.password(length=6)
    return name, email, password
