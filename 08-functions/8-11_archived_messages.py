def send_messages(messages):
    while messages:
        current_message = messages.pop()
        print(f"The message '{current_message}', has been sent!")
        sent_messages.append(current_message)

messages = ['Hello, my name is Hooman.', 'Life is good.', 'I am feeling grateful today.']
sent_messages = []

send_messages(messages[:])

print(f"messages: {messages}")
print(f"sent_messages: {sent_messages}")