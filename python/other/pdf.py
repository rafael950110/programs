from tika import parser

url = ['http://bizboard.nikkeibp.co.jp/houjin/cgi-bin/nsearch/md_pdf.pl/0000420219.pdf?NEWS_ID=0000420219&CONTENTS=1&bt=NSW&SYSTEM_ID=HO','http://bizboard.nikkeibp.co.jp/houjin/cgi-bin/nsearch/md_pdf.pl/0000418339.pdf?NEWS_ID=0000418339&CONTENTS=1&bt=LIN&SYSTEM_ID=HO']

for i in url :
	parsed = parser.from_file(i)
	print(parsed['metadata']['title'])