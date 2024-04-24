from models import User, db, add_to_database, print_all_users, get_user




user1 = User(login='std', password='1488', email='fdfdfd')

print(add_to_database(user1))
#print(print_all_users())
