import copy
from PIL import Image

with open("../updatelist") as f:
    content = f.readlines()
content = [x.strip() for x in content]

step = 1
track = 0

for s in content:
	if s == '%':
		track += 1
		continue
	if track < 2:
		continue

	doc = "../" + s
	img = Image.open(doc)
	data = img.getdata()
	x = data.size[0]
	y = data.size[1]

	MAX = 43
	if x > MAX:
		step = int(x/MAX)

	'''
	charlist = {}
	for i in range(33, 127):
		charlist.update( {i-33:chr(i)} )
	'''
	charlist = { 0:'`', 1:'\'', 2:'.', 3:',', 4:'\"',
				 5:'-', 6:'^', 7:':', 8:';', 9:'!',
				 10:'\\', 11:'/', 12:'(', 13:')', 14:'<',
				 15:'>', 16:'[', 17:']', 18:'{', 19:'}',
				 20:'=', 21:'+', 22:'*', 23:'@', 24:'%',
				 25:'$', 26:'&', 27:'#'}
	r = 3*256 / len(charlist)

	# covert pixel to char and store it into list
	lsts = []
	for j in range(0, y, step):
		lst = []
		for i in range(0, x, step):
			if data[j*x+i][3] == 0:
				lst.append(' ')
			else:
				lst.append( charlist[ int(sum(data[j*x+i][0:3])/r) ] )
		lst.append('\n')
		lsts.append(copy.deepcopy(lst))

	# output lst into .txt file
	new_doc = "../txt/" + doc.split('/')[2].split('.')[0] + ".txt"
	file = open(new_doc, "w")
	for i in range(len(lsts)):
		file.write(''.join(lsts[i]))