'''
CRUD 

DataBase

Terminal View

UX - add Email and Message (CRUD)

'''

DataBase: dict = dict()

_id = 0

def create_data(email: str, message: str):
    '''
    add object in Database
    '''
    global _id 
    obj = {
        'email': email, 
        'message': message
    }
    DataBase[_id] = obj 

    
    _id += 1 

def show_database(flag: bool) -> None:
    '''
    show all data in DataBase
    '''
    if flag:
        for k, v in DataBase.items():
            print(k, v, '\n')
    else: 
        print(DataBase)        
    

for i in range(10):
    create_data(f'test{i}@test.com', 'hello it is SPAMMMMM')

show_database(flag=True)
print('-' * 50)

show_database(flag=True)


# TODO Read 
