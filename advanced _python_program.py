# Q. Take a input from the user, if a input given is a integer the follow the futher steps otherwise take the input again.
# If input=1 then, print the name of current file.
# If input=2then, create a folder test, at the present location
# If input=3 then, print IP address
# If input=4, then open browser and search for the site user has asked for
# If input=5, then open whatsapp and send message to the number you want to send message to.

while True:
    a = int(input("Enter a number between 1 to 5 : "))
    if a == 1:
        try:
            from pathlib import Path

            print(Path(__file__).stem)
        except OSError:
            pass
    elif a == 2:
        import os

        d = os.path.dirname(__file__)  # directory of script
        p = r'{}/Test'.format(d)  # path to be created
        try:
            os.makedirs(p)
            print("test folder is created")
        except OSError:
            pass
    elif a == 3:
        try:
            import socket

            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
            print("Your Computer Name is:" + hostname)
            print("Your Computer IP Address is:" + IPAddr)
        except OSError:
            pass
    elif a == 4:
        try:
            import webbrowser

            webbrowser.open('<Site you want to open>')
        except OSError:
            pass
    elif a == 5:
        try:
            import pywhatkit

            pywhatkit.sendwhatmsg_instantly("<number with country code>", "<Message you wanna type")
        except OSError:
            pass
    else:
        break
