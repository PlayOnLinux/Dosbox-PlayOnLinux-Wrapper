#!/usr/bin/python
import sys, string

tmp = sys.argv[1]
tmp = string.split(sys.argv[1],"\\")
i = 0
for content in tmp:
	content2 = string.split(content,".")
	if(len(content2[0]) > 8):
		content2[0] = content2[0][0:6]+"~1" ## Fixme, we should consider the case if there are several files
		content = string.join(content2,".")
	tmp[i] = content
	i+=1
	
tmp = string.join(tmp,"\\")
tmp = tmp.upper()
print tmp