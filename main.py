from cellphone import CellPhone

cellphone_one = CellPhone("xxx")

# print the cell phone's contacts
print("all contacts in my cell", cellphone_one.contacts)


cellphone_one.receive_messages("hello world 1")
cellphone_one.receive_messages("hello world 2")

# print receive messages
print(cellphone_one.messages)

# create message and send to selected contacts
cellphone_one.create_message()


# toggle phone vibration
cellphone_one.toggole_vibrate(False)
print(cellphone_one.is_vibrate_on)
