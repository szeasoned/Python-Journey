words = [["hey", "hey", "hey"],
         ["hoh", "hoh", "hoh"],
         ["heh", "heh", "heh"]
    ]
for x in words: # iterates through each sublist in words[]. x = each sublist (e.g. ["hey", "hey", "hey"]). runs 3 times total
    for y in x: # iterates through each string in the current sublist x. y = each string (e.g. "hey", "hoh")
        print(y, end='') # prints each string without a newline
    print() # moves to the next line after each full sublist is printed
