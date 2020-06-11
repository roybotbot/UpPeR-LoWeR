#!/usr/local/bin/python

sTrInG = input("PaStE In sTrInG YoU WaNt tO cHaNgE: ").lower()

nEw_StRiNG = ""
iNdEx = 0
for i in sTrInG:
	if i != " " and iNdEx % 2 == 0:
			nEw_StRiNG += i.upper()
	else:
		nEw_StRiNG += i
	iNdEx += 1

print(nEw_StRiNG)