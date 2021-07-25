import hashlib
import os
a = input("Enter 1 file location: ")
b = input("Enter 2 file location: ")
c = input("Enter data store file location: ")
with open(a) as f:
    d = f.read()
with open(b) as f:
    e = f.read()
    d += "\n"
    d += e
with open("add.txt","w") as f:
    f.write(d)

completed_lines_hash = set()
output_file = open(c, "w")

for line in open("add.txt", "r"):

  hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()

  if hashValue not in completed_lines_hash:
    output_file.write(line)
    completed_lines_hash.add(hashValue)

output_file.close()

os.remove("add.txt")
