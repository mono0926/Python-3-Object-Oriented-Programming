import sys
filename = sys.argv[1]

contacts = []
with open(filename) as file:
    header = file.readline().strip().split('\t')
    for line in file:
        line = line.strip().split('\t')
        contact_map = zip(header, line)
        contacts.append(dict(contact_map))

for contact in contacts:
    print("email: {email} -- {last}, {first}".format(
        **contact))
