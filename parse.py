import json	
import re
import os
# -*- coding: utf-8 -*-

def rpl(fil):
	if (os.path.getsize(fil) > 300):
		print(fil)
		with open(fil, "r+") as f:
			data = json.load(f)
			if isinstance(data,list):
				for word in data:
					for w in word:
						#print(type(word[w]))
						if not isinstance(word[w],list):
							for key in d.keys():
								word[w] = re.sub(rf"{key}([\]-.,:\s]]|$)", rf"{d[key]}\1", word[w], flags=re.IGNORECASE)
			else:				
				for word in data:
					for w in data[word]:
						if isinstance(data[word][w],list):
							for ww in data[word][w]:
								for key in d.keys(): 
									ww = re.sub(rf"{key}([-.,:\s]]|$)", rf"{d[key]}\1", ww, flags=re.IGNORECASE)

						else:
							for key in d.keys(): 
								data[word][w] = re.sub(rf"{key}([-.,:\s]]|$)", rf"{d[key]}\1", data[word][w], flags=re.IGNORECASE)
		with open(fil, "w") as f:
			json.dump(data,f, indent=4)
	




keyw="kwords"
d = {}

with open(keyw,"r+") as dicti:
	lines=dicti.readlines()
	for l in lines:
		a = l.split(" ")
		print(a)
		d[a[0]]=a[1].rstrip("\n")
		d["#y"+a[0]]="#y" + a[1].rstrip("\n")
		d["#y"+a[0]+"s"]="#y" + a[1].rstrip("\n")
		d[a[0]+"s"]=a[1].rstrip("\n")
		d["#g"+a[0]]="#g" + a[1].rstrip("\n")
		d["#g"+a[0]+"s"]="#g" + a[1].rstrip("\n")
		d["#r"+a[0]]="#r" + a[1].rstrip("\n")
		d["#r"+a[0]+"s"]="#r" + a[1].rstrip("\n")
		#print(d)
print(os.getcwd())
dir=os.getcwd()
for file in os.listdir(dir):
	if file.endswith(".json"):
		rpl(file)
'''
fl="x.txt"
with open(fl,"w") as f:
	json.dump(d,f, indent=4)	
'''
'''
with open(filecard, "r+") as f:
	data = json.load(f)
	for word in data:
		for key in d.keys(): 
			data[word]["DESCRIPTION"] = re.sub(rf"{key}([.,\s]|$)", rf"{d[key]}\1", data[word]["DESCRIPTION"], flags=re.IGNORECASE)
			if "UPGRADE_DESCRIPTION" in data[word].keys():
				data[word]["UPGRADE_DESCRIPTION"] = re.sub(rf"{key}([.,\s]|$)", rf"{d[key]}\1", data[word]["UPGRADE_DESCRIPTION"], flags=re.IGNORECASE)
#print(data)
'''
'''
with open(filecard, "w") as f:
	json.dump(data,f, indent=4)
'''
		

