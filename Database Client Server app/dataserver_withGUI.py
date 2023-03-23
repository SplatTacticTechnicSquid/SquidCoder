
import PySimpleGUI as sg
import time
import threading

#we need to make the function to communicate with user

#well since we cannot just randomly connect to a server - ask the user somethin
import PySimpleGUI as sg
import time
import threading
# Add some color
# to the window
sg.theme('DarkBlue')     
  
# Very basic window.
# Return values using
# automatic-numbered keys

def closewindowtimer(seconds, window):
    global count
    count = 0
    while count <= seconds:
        count += 1
        time.sleep(1)
        
    window.write_event_value('Alarm', "1 minute passed")

layout = [
    [sg.Text('PLEASE ENTER IP AND PORT ADDRESS')],
    [sg.Text('IP ADDRESS', size =(15, 1)), sg.InputText()],
    [sg.Text('PORT ADDRESS', size =(15, 1)), sg.InputText()],
    [sg.Submit('Ok'), sg.Cancel()]
]
  

window = sg.Window('Simple data entry window', layout)
while True:
    try:

        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Cancel':
            break #if the event WIN_CLOSED user presses X or cancels the button = then stop program

        elif event == 'Start':
            threading.Thread(target=closewindowtimer, args=(10, window), daemon=True).start()

        elif event == 'Alarm':
            message = values[event]
            sg.popup_auto_close(message)
            break
    
        print(event, values[0], values[1])
        print(values[0])
        temp1 = values[0]
        #what caused the error is that you used int(values[0]) - that's the problem cause separated values are not integer type.. >:(
        temp2 = int(values[1])

        print(temp1, temp2, "values entered")

        window.close()


    except ValueError:
        sg.Popup("   ", "Error! Invalid input. Please try again", "   ")
        
        print("   ", "Error! Invalid input. Please try again", "   ",)
        

if temp1 and temp2 != 0:
    HOST = temp1
    PORT = temp2

print(HOST)

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

    # def sgpopup():
    #     sg.Popup("   ","server is listening on {}".format(HOST), "   ")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen() # this will make the server listen to client
        print("server is listening on {}".format(HOST))
        #sgpopup()
        while True:
            conn, addr = server.accept()
            #sg.Popup("   ","server is listening on {}".format(HOST), "   ")
            print("connected")
            handle_client(conn)
            print(conn, "data of conn")
            writetofile()
            #sgpopup()
            #searchquery()




except OSError as error :
    print(error)
    print("Error, cannot retrive client data connection to database")

    #note the client, will not have the source code - they will only just send data to server. That's it