from database import SessionLocal
from models import User, Order
from faker import Faker
import random

fake = Faker()
db = SessionLocal()

print("Creating users...")
users = []
for _ in range(150000):
    user = User(
        name=fake.name(),
        email=fake.email()
    )
    users.append(user)

db.bulk_save_objects(users)
db.commit()

print("Creating orders...")
for _ in range(600000):
    order = Order(
        user_id=random.randint(1, 100000),
        amount=random.uniform(10, 1000)
    )
    db.add(order)

db.commit()
db.close()

print("Data inserted successfully")
