#!usr/bin/env python3
import pyperclip as pycp

# gets clipboard and assigns to sTrInG
sTrInG  = pycp.paste()

NeW_StRiNg = ""
iNdEx = 0
for i in sTrInG:
	if i != " " and iNdEx % 2 == 0:
			NeW_StRiNg += i.upper()
	else:
		NeW_StRiNg += i
	iNdEx += 1

# copies NeW_StRiNg to keyboard
pycp.copy(NeW_StRiNg)