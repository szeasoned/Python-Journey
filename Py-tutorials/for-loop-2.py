values = ((1, 2, 3),
          (4, 5, 6),
          (7, 8, 9),
          ("*", 0, "#"))

for x in values:
    for y  in x:
        print(y, end='')
    print()