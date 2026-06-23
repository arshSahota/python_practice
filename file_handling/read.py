# reading a file

# with open("file.txt", "r") as f:
#     content = f.read()
#     print(content)

# writing to a file

# with open("file.txt", "w") as f:
#     f.write("Hello world")

#important ==> w overwrites the file

#appendind to a file

# with open("file.txt", "a") as f:
#     f.write("\nwritten by Arshdeep")

# why with open ==> because it automatically closes the file 

with open("names.txt", "r") as f:
    count = 0
    for line in f:
        if line.strip():
            count+=1
    print(f"Total names: {count}")