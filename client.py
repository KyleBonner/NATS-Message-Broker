import socket
import sys

#VARIABLE
try:    
    client_type  = sys.argv[1]
    client_subject = sys.argv[2]
    client_message = sys.argv[3]
except:
    print("Arguments Invalid")
    sys.exit()


print("This is a client")
print("type:", sys.argv[1])
print("subject:", sys.argv[2])
print("message:", sys.argv[3])

