# Python Program to compute
# MAC address of host
# using UUID module

import uuid

# printing the value of unique MAC
# address using uuid and getnode() function
print(hex(uuid.getnode()))

# Python 3 code to print MAC
# in formatted way.

import uuid

# joins elements of getnode() after each 2 digits.

print("The MAC address in formatted way is : ", end="")
print(':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
                for ele in range(0, 8 * 6, 8)][::-1]))

# Python 3 code to print MAC
# in formatted way and easier
# to understand

import re, uuid

# joins elements of getnode() after each 2 digits.
# using regex expression
print("The MAC address in formatted and less complex way is : ", end="")
print(':'.join(re.findall('..', '%012x' % uuid.getnode())))

# Python Program to Get IP Address
import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)

