#!/usr/local/bin/python

import subprocess 

sTrInG = input("PaStE In sTrInG YoU WaNt tO cHaNgE: ").lower()

NeW_StRiNg = ""
iNdEx = 0
for i in sTrInG:
	if i != " " and iNdEx % 2 == 0:
			NeW_StRiNg += i.upper()
	else:
		NeW_StRiNg += i
	iNdEx += 1

subprocess.run("pbcopy", universal_newlines=True, input=NeW_StRiNg)
print("\"" + NeW_StRiNg + "\"" + " has been copied to the clipboard.")