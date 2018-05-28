from subprocess import Popen, CREATE_NEW_CONSOLE

# Client processes list
p_list = []

while True:
    user = input('Start multiple clients (s) / Close clients (x) / Quit (q)' + '\n' + '>> ')

    if user == 'q':
        break
    elif user == 's':
        n = input('How many clients to start: ')
        for _ in range(int(n)):
            # Start 5 processes in separate console window
            p_list.append(Popen('py client.py', creationflags=CREATE_NEW_CONSOLE))

        print(f'{n} clients started\n')

    elif user == 'x':
        for p in p_list:
            p.kill()
        p_list.clear()
    else:
        print('Wrong input!')
