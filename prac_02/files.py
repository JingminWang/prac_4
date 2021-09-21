name = input("Name:")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

f=open('name.txt','r')
data=f.read()
print("Your name is {}".format(data))
f.close()

sum = 0
f = open("numbers.txt", 'r')
for i in range(2):
    a = f.readline()
    sum += int(a)
    print(a)
print(sum)
f.close()

f = open("numbers.txt", 'r')
total = 0
text_lines = f.readlines()
for line in text_lines:
    total += int(line)
print(total)
