file = open("p022_names.txt", "r")
names = file.read().split(',')
file.close()

for i in range(len(names)):
    names[i] = names[i][1:-1].lower()
names = sorted(names)

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

sum = 0
for i in range(len(names)):
    name_sum = 0
    for k in range(len(names[i])):
        name_sum += alpha.index(names[i][k])+1
    sum += name_sum*(i+1)
    
print(sum)
