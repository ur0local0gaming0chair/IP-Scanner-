from twilio.rest import Client
import os

print("Network Scanner  ")
print("   by Depp  \n")

account_sid = "your sid" #in a " x " format
auth_token = "your token"

client = Client(account_sid, auth_token)
signals = 0
sig = 1

def output_text():
    with open("D:\\ip_list.txt") as file:       #create a ip_list.txt in your D:// drive and put your ip address in there
        dump = file.read()
        dump = dump.splitlines()

    for ip in dump:
        res = os.popen(f"ping {ip}").read()
        if (("unreachable") or ("Request time out")) in res:

            f = open("D\\output.txt", "a")
            f.close()
            print("ip address is close")

        else:
            f = open("D:\\output.txt", "a")
            f.close()
            print("ip address is close")


    with open("D:\\output.txt") as file:
        output = file.read()
        print(output)

    with open("D:\\output.txt", "w") as file:       #the output.txt file needs to be empty
        pass


def send():                    #in a " x " format          #in a " x " format
    client.messages.create(to="YOUR PHONE NUMBER", from_="YOUR TWILIO PHONE NUMBER", body=ip + " is connected")
    signals == sig
    if sig == 1:
        print("\nphone signal sent\n")
        while True:
            output_text()

while True:
    try:         #checking for the ip
        with open("D:\\ip_list.txt") as file:
            dump = file.read()
            dump = dump.splitlines()

        for ip in dump:
            res = os.popen(f"ping {ip}").read()
            if (("unreachable") or ("Request time out")) in res:

                print("\nscanning ip address >>  " + ip + "\n")
                f = open("D\\output.txt", "a")
                f.close()
                print("ip address is close")
                send()

            else:
                print("\nscanning ip address >>  " + ip + "\n")
                f = open("D:\\output.txt", "a")
                f.close()
                print("ip address is close")
                send()

        with open("D:\\output.txt") as file:
            output = file.read()
            print(output)

        with open("D:\\output.txt", "w") as file:
            pass
    except:
        print("no signal detected")