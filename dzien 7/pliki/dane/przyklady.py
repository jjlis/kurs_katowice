#fh = opne('logs.txt')
#print(dir(fh))

#fh.close()

with open("logs.txt") as logi, open("emails.txt") as emaile:
    print(logi.read())
    print(emaile.read())

for line in f:
    print(line)