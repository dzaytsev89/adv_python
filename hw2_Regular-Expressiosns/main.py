import csv
import re


def contact_fill(row):

    lastname = re.findall(r'\w+', row[0])
    firstname = re.findall(r'\w+', row[1])
    surname = re.findall(r'\w+', row[2])
    phone_pattern = (
        r'(\+7|8)[\s|\(]*(\d{3})[\)\s*-]?\s*(\d{3})[-\s]?(\d.)[-\s]?(\d+)\s*[\(\s*]?(\w+.)?\s*(\d+)?[\)\s?]?')
    phone_sub = r'+7(\2)\3-\4-\5 \6\7'
    contact = []
    contact.extend(lastname)
    contact.extend(firstname)
    if len(contact) <= 2 and len(surname) == 0:  # if no surname at all
        contact.append('')
    else:
        contact.extend(surname)
    contact.append(row[3])  # organization
    contact.append(row[4])  # position
    contact.append(re.sub(phone_pattern, phone_sub, row[5]).rstrip())
    contact.append(row[6])  # mail
    return contact


def merge_contact(contact, book):
    for p in book:
        if p == contact:
            continue
        elif p[:2] == contact[:2]:  # check for duplicate by firstname and lastname
            for i in range(len(contact)):
                if contact[i] == p[i]:
                    continue
                if p[i] == "":
                    p[i] = contact[i]
            break
    return contact, book


phonebook = []

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=',')
    contact_list = list(rows)
    header = contact_list.pop(0)
    phonebook.append(header)
    for c in contact_list:
        person = contact_fill(c)
        merge_contact(person, phonebook)
        if person[:2] in [p[:2] for p in phonebook]:
            continue
        else:
            phonebook.append(person)

print(*phonebook, sep='\n')

with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(phonebook)
