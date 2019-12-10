import os

for member in dir(os.path):
    print(member)

print(os.path.curdir)
print(os.path.join("../..", ".."))