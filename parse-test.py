import json	
import re
import os
# -*- coding: utf-8 -*-
def unescape(in_str):
    """Unicode-unescape string with only some characters escaped."""
    return in_str.encode('unicode-escape').replace(b'\\\\u', b'\\u').decode('unicode-escape')


def rpl(fil):
	if (os.path.getsize(fil) > 300):
		print(fil)
		with open(fil, "r+", encoding='utf-8') as f:
			data = json.load(f)
			if isinstance(data,list):
				for word in data:
					for w in word:
						#print(type(word[w]))
						if not isinstance(word[w],list):
							for key in d.keys():
								word[w] = re.sub(rf"{key}([\(\-.,:\s\]]|$)", rf"{'ццц'}\1", word[w], flags=re.IGNORECASE | re.UNICODE)
								#word[w] = unescape(word[w])
			else:				
				for word in data:
					for w in data[word]:
						if isinstance(data[word][w],list):
							for lst in data[word][w]:
								for key in d.keys(): 
									lst = re.sub(rf"{key}([\(\-.,:\s\]]|$)", rf"{'ццц'}\1", lst, flags=re.IGNORECASE | re.UNICODE)
									#lst = unescape(lst)
						else:
							for key in d.keys():
								#print(w) 
								data[word][w] = re.sub(rf"{key}([\(\-.,:\s\]]|$)", rf"{'ццц'}\1", data[word][w], flags=re.IGNORECASE | re.UNICODE)
								#data[word][w] = unescape(word[w])
		with open(fil, "w", encoding='utf-8') as f:
			json.dump(data,f, indent=4, ensure_ascii=False)
	else:
		print("file " + fil + " is too small")




keyw="kwords"
d = {}

with open(keyw,"r+") as dicti:
	lines=dicti.readlines()
	for l in lines:
		a = l.split(" ")
		#print(a)
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
		

