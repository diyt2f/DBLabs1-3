import psycopg2
import Model
import View
import Controller


# Execute a query
#Model.add_author(15, 'TestPsychopg')

records = Model.get_author(15)
print(records[0][1])

#Model.add_book(15, 'TestBook1', 129, 52)
# Model.add_client(15, 'Test', 'Login231', 'A4@gmail.com')
# Model.add_purchase(15, 15, 501, 'UA342342')
# records = Model.get_book(15)
# records = Model.get_client(15)
# print(records)
# records = Model.get_purchase(15)
# print(records)
# Model.update_author(15, 'Updated1')
# Model.update_book(15, 'Updated1', 15, 15)
# Model.update_purchase(15, 15, 15, 'TEST1')
# Model.update_client(15, 'Updated', 'Updated', 'Updated')
Controller.open_menu()