# To read a file 

# The basics
file = open('test.txt')
#file.read()     #read all the contents (by defult when leaving the bracket empty) of the file, and Python will put a bookmark at the end of the file. This will cause it to pick it up again from the bookmark (end of file) when I have a command to read it again to print the content (just like the next line), which will return empty content.
print(file.read())  #print it so that we can see that python can read it.
file.close()

# Modern style:
print("Modern Python Style:")
with open('test.txt') as file:
    content = file.read()
    print(content)
# No need of 'file.close(), file is closed once reach the end of the 'with' block

# Read selected # of characters/bytes from the file, the basic way
with open('test.txt') as file:
    content = file.read(10)
    print(content)

with open('test.txt') as file:
    contentLine = file.readline()   #read 1 single line. If want to read more lines, will need to write more of this line, which violates the 'DRY' principle.
    print(contentLine)      # Since Python already read the 1st 10 characters, the 'bookmark' is placed at the 10th character and when executing .readline(), it's starting from there to read the rest of the 1st line.

# Instructor's styles of reading all lines with loop:
# 1st: 
file = open('test.txt')
line = file.readline()
while line!="":
    print(line)
    line = file.readline()  # In order for python to move on to reading the next line, we need this step within the loop, otherwise, it get stucked in printing the 1st line forever.
file.close()

# 2nd:
file = open('test.txt')
for line in file.readlines():   # Reads and stores every line of the file in a "container" at this step, which will take up memory space.
    print(line)                 # Reading the 2nd time to print each line
file.close()

# Compare with my alternative version:
file = open('test.txt')
for line in file:       # Reads one line at a time (streaming), and doesn't take up much memory usage.
    print(line)         # Instant start to print each line
file.close()

# This is a way to write more simple codes, but the 本质 of taking up all the memory spaces from r4eading & storing the entire file doesn't optimize it, and may poses as a potential memory crush hazard in real-world scenarios, where the file gets over 50G. 
with open('test.txt', 'r') as file:
    for line in file.readlines():
        print(line)

# The industry standard way:
print("The Industry Standard:")
with open('test.txt', 'r') as file: #'r' = read only mode, defult mode even without explicitly writing it out, but good practice to write.
    for line in file:
        print(line.strip()) # Removing the hidden '\n' (new line) at the end of each line, which will no longer creat the another new/empty line with the print() function.






