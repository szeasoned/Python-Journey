calc = [(1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        ("*", 0, "#")
        ]

for values in calc:
    for value in values:
        print(value, end=" ")
    print()