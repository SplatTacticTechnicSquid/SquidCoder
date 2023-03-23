#we need to make the function to communicate with user

#well since we cannot just randomly connect to a server - ask the user somethin
print("you need to input both the host and port number")

while True:
    try:
        HOSTINPUT = input("input the host number: \n")
        PORTINPUT = int(input("input the port number: \n"))
        
        if isinstance(HOSTINPUT, int) == False:
            break

        elif isinstance(PORTINPUT, int) == False:
            break
        
        else:
            continue
    except ValueError:
        print('data type invalid, please re enter')

#HOST = '10.6.6.1'
#PORT = '2004'
HOST = HOSTINPUT
PORT = PORTINPUT

import socket

try:

    # #def handle_database(checkconnection):
    #     databit = checkconnection.recv(1024) #1024checkconnection bits
    #     #make data transfer work
    #     inputtoserver = databit.decode()
    #     with open('databasestudent.txt', 'a') as fileprocess:
    #         fileprocess.write(inputtoserver)

    #     checkconnection.send("the data has been saved")
    #     checkconnection.send(inputtoserver)
    #     checkconnection.close()
            
    #     if __name__ == '__main__':
    #         handle_database()


    def handle_client(conn):
        data = conn.recv(1024)
        global expression
        expression = data.decode()
        print(expression)
        conn.send(str(expression).encode())
        conn.close()


    def writetofile():
        with open("databaselist.txt", 'a') as file:
            file.write("{}, \n".format(expression))
    
    # def searchquery():
    #     with open("databaselist.txt", 'a') as file:
    #         searchterm = expression
    #         flag = 0
    #         for x in file:
    #             student_number, name = x.strip().split(',')
    #             if searchterm in name:
    #                 flag = 1
    #                 print("student name found")
    #             if not flag:
    #                 print("safe")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen() # this will make the server listen to client
        print("server is listening on {}".format(HOST))
        while True:
            conn, addr = server.accept()
            print("connected")
            handle_client(conn)
            print(conn, "data of conn")
            writetofile()
            #searchquery()




except OSError as error :
    print(error)
    print("Error, cannot retrive client data connection to database")

    #note the client, will not have the source code - they will only just send data to server. That's it