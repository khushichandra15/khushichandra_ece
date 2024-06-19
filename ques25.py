f1 = open("samplefile1.txt", "r")
f2 = open("samplefile2.txt", "a")
for line in f1: 
    f2.write(line)
print("done!")