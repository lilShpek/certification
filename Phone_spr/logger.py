import os

def input_contact():
    # f = open('data.txt', 'r')
    # if not f:
    #     f = open('data.txt', 'w')
    #     f.close()
    # else:
    #     f.close()
    if not os.path.isfile('data.txt'):
        f = open('data.txt', 'w')
        f.close()


    with open('data.txt', 'a', encoding='utf-8') as f:
        user = input('Введите имя, фамилию и телефон: ').strip().split()
        f.write(';'.join(user) + '\n')


def print_contacts():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
    for contact in contacts:
        print(*contact.strip().split(';'))


def find_contact():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
    while True:
        print('По каким параметрам ищем контакт?:\n1. Имя\n2. Фамилия\n3. Телефон')
        command_index = int(input('Команда: '))
        if str(command_index) not in '123':
            print('Других параметров нету.')
        else:
            break
    data = input('Введите данные: ')
    print('Найденные контакты: ')
    for contact in contacts:
        full_contact = contact.strip().split(';')
        if data == full_contact[command_index-1]:
            print(' '.join(full_contact))

def update_contact():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()

    data_to_change = input('Введите имя, фамилию или телефон контакта для изменения: ')
    updated_data = input('Введите новые данные через пробел (имя, фамилия, телефон): ')

    updated_contacts = []
    updated = False

    for contact in contacts:
        full_contact = contact.strip().split(';')
        if len(full_contact) >= 3 and data_to_change in (full_contact[0], full_contact[1], full_contact[2]):
            updated_contacts.append(';'.join(updated_data.split()) + '\n')
            updated = True
        else:
            updated_contacts.append(contact)

    if updated:
        with open('data.txt', 'w', encoding='utf-8') as f:
            f.writelines(updated_contacts)
            print('Данные успешно изменены.')
    else:
        print('Контакт не найден.')

def delete_contact():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()

    data_to_delete = input('Введите имя или фамилию контакта для удаления: ')

    updated_contacts = []
    deleted = False

    for contact in contacts:
        full_contact = contact.strip().split(';')
        if len(full_contact) >= 3 and data_to_delete in (full_contact[0], full_contact[1], full_contact[2]):
            deleted = True
        else:
            updated_contacts.append(contact)

    if deleted:
        with open('data.txt', 'w', encoding='utf-8') as f:
            f.writelines(updated_contacts)
            print('Контакт успешно удален.')
    else:
        print('Контакт не найден.')



