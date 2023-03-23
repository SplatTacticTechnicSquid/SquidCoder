import PySimpleGUI as sg
import time
import threading
# Add some color
# to the window
sg.theme('DarkGreen4')     
  
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

# windows = sg.Window('CLIENT Window', layout)
# try:
#     while True:
#         event, values = windows.read()
#         if event == sg.WIN_CLOSED or event =='Cancel':
#             break
#         print('you entered', values[0])
#     windows.close()
# except OSError:
#     print("error, cannot render window")

import random as rd

#print("enter the HOST and PORT of the server you are trying to communicate: \n")

# while True:
#     try:
#         #HOSTINPUT = input("input the host number: \n")
#         #PORTINPUT = int(input("input the port number: \n"))
#         HOSTINPUT = values[0]
#         PORTINPUT = values[1]
#         if isinstance(HOSTINPUT, int) == False:
#             break
#         elif isinstance(PORTINPUT, int) == False:
#             break

#         else:
#             continue

#     except ValueError:
#         print("invalid input")

secondlayout = [
    [sg.Text('PLEASE ENTER STUDENT NUMBER AND STUDENT NAME')],
    [sg.Text('STUDENT NUMBER', size =(15, 1)), sg.InputText()],
    [sg.Text('STUDENT NAME', size =(15, 1)), sg.InputText()],
    [sg.Submit('Enter'), sg.Cancel()]
]

windowsecond = sg.Window('Simple data entry window', secondlayout)
while True:
    try:
        event, valuestudent = windowsecond.read()

        if event == sg.WIN_CLOSED or 'Cancel':
            break
    
        elif event == 'Start':
            threading.Thread(target=closewindowtimer, args=(10, windowsecond), daemon=True).start()

        elif event == 'Alarm':
            message = valuestudent[event]
            sg.popup_auto_close(message)
            break

        
        

        windowsecond.close()

    except ValueError:
        sg.Popup("   ", "Error! Invalid input. Please try again", "   ")
        print("error, invalid inputs")

temp3 = valuestudent[0]
temp4 = valuestudent[1]

import socket
try:
    while True:
        global student_uid, student_number, student_name

        student_uid = rd.randint(1000, 9999)
        #student_number = int(input("please input the user number: \n"))
        #student_name = input("input the student name \n")

        student_number = temp3
        student_name = temp4

        def finalevaluate(a,b,c):

            finalreport = "{}, {}, {}".format(a, b, c)
            print(finalreport)

            return finalreport


#note that this will be used to SEND ONLY

        try:
            x = finalevaluate(student_uid, student_number, student_name)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.send(x.encode())
                resultend = s.recv(1024)
        except ValueError:
            print("error in connection config")

#just a loop if user wants to continue
        inputtocontinue = 1 #flag
        #array of allowed keywords
        allowedarg = ["yes", "y", "Y", "YEA"]
        #prompt the user:
        entercontinue = input("do you want to continue the code?")

        if entercontinue not in allowedarg:
            inputtocontinue = 0
        #elif entercontinue == "Yes" or "yes" or "y":
        elif any(element in entercontinue for element in allowedarg):
            print("ok")
            inputtocontinue = 1
        
        if inputtocontinue == 0:
            break
        else:
            continue

except OSError as error :
    print(error)
    print("Error, cannot establish connection to database")