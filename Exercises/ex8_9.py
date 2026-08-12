def show_message(text_list):
    for text in text_list:
        print(text)

def send_messages(text_list, sent_messages):
    while text_list:
        message = text_list.pop(0)
        sent_messages.append(message)

text_list = ['a', 'b', 'c']
sent_messages = []

show_message(text_list)
send_messages(text_list[:], sent_messages)

print(text_list)
print(sent_messages)