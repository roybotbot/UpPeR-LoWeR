#!/usr/local/bin/python3

import subprocess 
import pyperclip as pycp

sTrInG  = pycp.paste()

NeW_StRiNg = ""
iNdEx = 0
for i in sTrInG:
	if i != " " and iNdEx % 2 == 0:
			NeW_StRiNg += i.upper()
	else:
		NeW_StRiNg += i
	iNdEx += 1

subprocess.run("pbcopy", universal_newlines=True, input=NeW_StRiNg)