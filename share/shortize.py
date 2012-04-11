#!/usr/bin/python
import sys, string

tmp = sys.argv[1]
tmp = string.split(sys.argv[1],"\\")
i = 0
for content in tmp:
	if(len(content) > 8):
		content = content[0:6]+"~1" ## Fixme, we should consider the case if there are several files
	tmp[i] = content
	i+=1
	
tmp = string.join(tmp,"\\")
tmp = tmp.upper()
print tmp