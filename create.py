from models import User, db, add_to_database, print_all_users




user1 = User(login='std', password='1488')

print(add_to_database(user1))
print(print_all_users())