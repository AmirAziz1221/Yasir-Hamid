import pywhatkit as kit
import time

# Set the recipient's phone number and the message
phone_number = "+1234567890"  # Replace with the recipient's phone number (include the country code)
message = "Hello, this is a test message!"

# Send the message 1000 times
for i in range(1000):
    try:
        # Sends the message immediately
        kit.sendwhatmsg_instantly(phone_number, message)
        print(f"Message {i + 1} sent successfully!")
        
        # Adding a short delay to avoid spamming too fast
        time.sleep(2)  # Adjust the time if needed
    except Exception as e:
        print(f"An error occurred: {e}")
        break
