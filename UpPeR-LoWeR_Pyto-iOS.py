# UpPeR-LoWeR_iOS.py

import sys

sTrInG = sys.argv[1]

NeW_StRiNg = ""
iNdEx = 0
for i in sTrInG:
	if i != " " and iNdEx % 2 == 0:
			NeW_StRiNg += i.upper()
	else:
		NeW_StRiNg += i
	iNdEx += 1

print(NeW_StRiNg)


