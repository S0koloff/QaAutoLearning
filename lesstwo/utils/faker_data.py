from faker import Faker

fake = Faker()

def generate_user_data():
    return {
        "name": fake.first_name(),
        "job": fake.job(),
        "email": fake.email(),
        "password": fake.password(length=10)
    }

def generate_user_name_job_data():
    return {
        "name": fake.first_name(),
        "job": fake.job()
    }