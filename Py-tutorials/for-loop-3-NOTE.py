words = ["hey", "hey", "hey",
         "hoh", "hoh", "hoh",
         "heh", "heh", "heh"
    ]
for x in words: # iterates through each item in words[]. x = each string (e.g. "hey", "hoh"). runs 9 times total
    for y in x: # iterates through each character in the current string x. y = each character (e.g. "h", "e", "y")
        print(y, end='') # prints each character without a newline
    print() # moves to the next line after each full string is printed
