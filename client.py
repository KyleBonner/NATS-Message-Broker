import socket
import sys

try:    
    ip =   sys.argv[1]
    port = sys.argv[2]
    client_type    = sys.argv[3]
    client_subject = sys.argv[4]
except:
    print("Arguments Error")
    sys.exit()

try:
    if sys.argv[3] != "request" and sys.argv[3] != "reply":
        print("Invalid subject")
        sys.exit()
except:
    print("Subject input Error")
    sys.exit() 

    #Bug may occur here if the message arguments are not properly concatenated

try:
    message = ' '.join(sys.argv[5:])
except:
    print("Message concatenation Error")
    sys.exit()

    
print("This is a client")
print("ip:", ip)
print("port:", port)
print("type:", client_type)
print("subject:", client_subject)
print("message:", message)
