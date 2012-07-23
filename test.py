import sys

text ="""Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"""

chars = list(text)

for char in chars:
    line = []
    while len(line) < 60:
        line[len(line):] = [chars.pop(0)]
        if line[len(line)-1] == " " and len(line) >= 55:
            break
    print "".join(line)