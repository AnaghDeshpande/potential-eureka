import pywhatkit as pywhatkit
import time

df = pd.read_excel("whatsapp.xlsx")

phone_number = ["Enter Phone Numbers in the form of list"]
message = "Enter Your Message Here"

for number in phone_number:
    try:
        pywhatkit.sendwhatmsg_instantly(number, message, tab_close=True, close_time=1)
        print("msg sent Successfully")
    except Exception as e:
        print(f"Failed to send message {e}")

