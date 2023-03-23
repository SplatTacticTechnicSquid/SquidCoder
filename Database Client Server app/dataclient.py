
import random as rd

print("enter the HOST and PORT of the server you are trying to communicate: \n")

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
        print("invalid input")

HOST = HOSTINPUT
PORT = PORTINPUT

import socket
try:
    while True:
        global student_uid, student_number, student_name

        student_uid = rd.randint(1000, 9999)
        student_number = int(input("please input the user number: \n"))
        student_name = input("input the student name \n")

        def finalevaluate(a,b,c):

            finalreport = "{}, {}, {}".format(a, b, c)
            print(finalreport)

            return finalreport


#note that this will be used to SEND ONLY


        x = finalevaluate(student_uid, student_number, student_name)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.send(x.encode())
            resultend = s.recv(1024)

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