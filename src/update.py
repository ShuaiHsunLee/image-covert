with open("../updatelist") as f:
    content = f.readlines()
content = [x.strip() for x in content]

lst1 = []
lst2 = []
diff = []
flag = 0

for s in content:
	if s == '%':
		flag += 1
		continue

	if flag == 0:
		lst1.append(s.split('/')[1].split('.')[0])
	elif flag == 1:
		lst2.append(s.split('/')[1].split('.')[0])

# list less file
flag_same = False
for i in lst1:
	flag_same = False
	for j in lst2:
		if i == j:
			flag_same = True
	if flag_same == False:
		diff.append(i)

# output diff into updatelist file
for k in diff:
	new_doc = "png/" + k + ".png\n"
	file = open("../updatelist", "a")
	file.write(new_doc)