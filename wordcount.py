import os

cwd = os.getcwd()
wds = open(cwd+'\subdir\muchText.txt')
d = dict()
for line in wds:
	for word in line.split():
		tok = word.strip().lower()
		d[tok] = d.get(tok, 0) + 1

sd = []
for tok in d:
	sd.append((d[tok], tok))

sd.sort(reverse=True)

for word in sd:
	count = word[0]
	if(count > 1):
		print(word[1], '\t', count)


ld = dict()
for word in sd:
	ld[word[0]] = ld.get(word[0], ()) + (word[1],)

for key in ld:
	if(key > 1):
		print(key, ld[key])
