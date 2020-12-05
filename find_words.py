import json	
import re
import os
# -*- coding: utf-8 -*-
def workfile(fil):
	with open(fil,"r+") as f:
		fa = f.read()
	fa = fa.replace("#y","")
	fa = fa.replace("#r","")
	fa = fa.replace("#b","")
	lst=re.findall(r"(\b[\w]+\b)",fa)
	for i in lst:
		d[(i.lower())] = d.get(i.lower(),0) + 1


def trydel(key):
	try:
		d.pop(key)
	except KeyError:
		print(f'Key {key} not found')
keyw="keywords"
d = {}

print(os.getcwd())
dir=os.getcwd()
for file in os.listdir(dir):
	if file.endswith(".json"):
		workfile(file)


with open("excluwords","r+") as fe:
	lines=fe.readlines()
	for l in lines:
		trydel(l.rstrip("\n"))


with open("qwords","w") as fl:
	for key in d.keys():
		if (d[key] > 4):
			fl.write(key+"\n")
