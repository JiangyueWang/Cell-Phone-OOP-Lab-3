class CellPhone:

    def __init__(self, model_type):
        self.model = model_type
        self.phone_number = ""
        self.contacts = {"person1": 12345678,
                         "person2": 12301233,
                         "person3": 12357890}
        self.messages = []
        self.is_vibrate_on = True

    def receive_messages(self, message):
        print(f'the message you received is : message')
        self.messages.append(message)

    def toggole_vibrate(self, is_vibrate):
        if is_vibrate == True:
            self.is_vibrate_on = is_vibrate
        else:
            self.is_vibrate_on = False

    def create_message(self):
        print("who you would like to send message to? please select from the list below ")
        for i in self.contacts.keys():
            print(i)
        self.message_to = input("")
        print("Enter the message you want to send")
        self.message = input("")
        print(
            f'you are going to to send message {self.message} to {self.message_to}')
