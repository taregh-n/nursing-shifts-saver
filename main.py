from module import *

make_database()

users = execute('SELECT * From Users')
if users:
    name =users[0][0]
    family = users[0][1]
    nurse_id = users[0][2]
else: 
    questions = insert_data(user = True)
    answers = inquirer.prompt(questions)
    name = answers['name']
    family = answers['family']
    nurse_id = answers['nurse_id']
    execute(f'INSERT INTO Users VALUES ("%s", "%s", "%s")' % (name, family, nurse_id))
nurse = Nurse(name, family, nurse_id)

print(f'Hello %s %s. ' % (name, family))

while True:
    while True:
        act = input('-> ')
        if act in ('brief', 'add', 'del', 'wp', 'add-wp', 'del-wp', 'month', 'exit'):
            break
        else:
            print('Invalid Input. Try again!')
    if act == 'brief':
        pass
    elif act == 'add':
        nurse.add_shift()
    elif act == 'del':
        nurse.del_shift()
    elif act == 'wp':
        nurse.workplaces_list()
    elif act == 'add-wp':
        nurse.add_workplace()
    elif act == 'del-wp':
        nurse.del_workplace()
    elif act == 'month':
        year = int(input('Year: '))
        month = int(input('Month: '))
        nurse.select_month(year, month)
    elif act == 'exit':
        break