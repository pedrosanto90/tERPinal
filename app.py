import database.db as db
# create an ID 
# create a client number

def createClient():
    db.connectDB()
# create id - generated by mysql
# create client number

    clientNumber = genClientNumber()

    name = input('Name: ')
    address = input('Address: ')
    telContact = input('Phone Number: ')
    emailContact = input('Email: ')
    
    db.insertClient(clientNumber, name, address, telContact, emailContact)

    print(f'Client Number: {clientNumber}')
    print(f'Name: {name}')
    print(f'Address: {address}')
    print(f'Phone Number: {telContact}')
    print(f'Email: {emailContact}')
    

def genClientNumber():

    clientNumber = 4521
    return clientNumber

createClient()

