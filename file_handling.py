"""
Python File Handling Program

r: Opens a file for reading only
r+: Opens a file for both reading and writing
w: Opens a file for writing only
w+: Open a file for writing and reading.
a: Opens a file for appending
a+: Opens a file for both appending and reading

read()                      readline()
readline()                  readlines()
fd                          seek()
tell()                      close()
truncate()

File Handling Operation:
output = open(r'C:\spam', 'w') Create output file ('w' means write)
input = open('data', 'r') Create input file ('r' means read)
input = open('data') Same as prior line ('r' is the default)
aString = input.read() Read entire file into a single string
aString = input.read(N) Read up to next N characters (or bytes) into a string
aString = input.readline() Read next line (including \n newline) into a string
aList = input.readlines() Read entire file into list of line strings (with \n)
output.write(aString) Write a string of characters (or bytes) into file
output.writelines(aList) Write all line strings in a list into file
output.close() Manual close (done for you when file is collected)
output.flush() Flush output buffer to disk without closing
anyFile.seek(N) Change file position to offset N for next operation
for line in open('data'): use line File iterators read line by line
open('f.txt', encoding='latin-1') Python 3.X Unicode text files (str strings)
open('f.bin', 'rb') Python 3.X bytes files (bytes strings)
codecs.open('f.txt', encoding='utf8') Python 2.X Unicode text files (unicode strings)
open('f.bin', 'rb') Python 2.X bytes files (str strings)
"""
import os
import shutil

def total_cound(file_name):
    word_count = 0
    line_count = 0
    char_cout  =  0
    with open(file_name, 'r' ) as fd:
        # This function uses the file iterator to iterate over the file
        # So we will read one line at a time. This is a memory efficient.
        for line in fd:
            print(line)
            line_count += 1
            char_cout += len(line)
            line = line.split(' ')
            word_count = len(line)
            print('line count = {0}, Word Count = {1} and Char Count = {2}'.\
            format(line_count, word_count, char_cout))


def readline_file(file_name):
    with open(file_name, 'r') as fd:
        #This function reads just one line. So for going next line we need to read it again
        # So this not time efficient
        line = fd.readline()
        while line:
            line = fd.readline()
            print(line)

def readlines_file(file_name):
    with open(file_name, 'r') as fd:
        #This reads the whole at a time in list
        #This is not memory efficient
        for line in fd.readlines():
            print(line)

def read_file(file_name):
    with open(file_name, 'r') as fd:
        #This reads whole file as string
        #This not a memory efficient
        line = fd.read()
        for line in line:
            print(line)

def os_module():
    # Python code to search .mp3 files in current
    # folder (We can change file type/name and path
    # according to the requirements.
    # This is to get the directory that the program
    # is currently running in.
    dir_path = os.path.dirname(os.path.realpath(__file__))

    for root, dirs, files in os.walk(dir_path):
        for file in files:

            # change the extension from '.mp3' to
            # the one of your choice.
            if file.endswith('.mp3'):
                print(root + '/' + str(file))

#One file has city and temp in the degree celcuis.
# WAP to convert the temp to fahrenheit and write to the same file.
def cel_to_farhenite(fileinput):
    with open(fileinput, 'r+') as fd, open("filename2", 'w') as fd1:
        for line in fd.readlines():
            city, temp = line.split(' ')
            farh = ((int(temp)*9)/5) + 32
            print(farh)
            str = "\n{0} {1}".format(city, farh)
            fd.write(str)

def file_copy():
    shutil.copy('filename1', 'filename2')

if __name__ == '__main__':
    #total_cound('filename')
    #readline_file('filename')
    #readlines_file('filename')
    #read_file('filename')
    #cel_to_farhenite('filename1')
    file_copy