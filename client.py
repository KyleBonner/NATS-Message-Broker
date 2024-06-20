import socket
import sys

try:    
    client_type  = sys.argv[1]
    client_subject = sys.argv[2]
    client_message = sys.argv[3]
except:
    print("Arguments Error")
    sys.exit()

try:
    if sys.argv[1] != "request" and sys.argv[1] != "reply":
        print("Invalid subject")
        sys.exit()
except:
    print("Subject input Error")
    sys.exit() 

    #Bug may occur here if the message arguments are not properly concatenated

try:
    message = ' '.join(sys.argv[3:])
except:
    print("Message concatenation Error")
    sys.exit()

    
print("This is a client")
print("type:", sys.argv[1])
print("subject:", sys.argv[2])
print("message:", message)
