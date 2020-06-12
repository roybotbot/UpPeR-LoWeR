# UpPeR-LoWeR_iOS.py

# afaik, to get this to work with iOS Shortcuts argv is needed
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

# shortcuts app takes printed output and copies to clipboard
print(NeW_StRiNg)