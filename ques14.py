lines = []
    while True:
        line = input("Enter a line (press Enter to stop): ")
        if line == "":
            break
        lines.append(line)
    
    if lines:
        print("\nAll lines entered:")
        for line in lines:
            print(line)
