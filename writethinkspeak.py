import urllib.request
msg=str(input('Enter your message : '))
msg = msg.replace(' ', "%20")
msg = msg.replace('\n', "%0A")
print("msg: ", msg)
b=urllib.request.urlopen('https://api.thingspeak.com/update?api_key=S0YP62ZBJGRY33DI&field1='+msg)
print("\nYour message has successfully been sent!")