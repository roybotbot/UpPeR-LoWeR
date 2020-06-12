#!/usr/local/bin/python3

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

pycp.copy(NeW_StRiNg)