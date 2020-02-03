import key

#entry = open('input.txt', 'r')
#inbox = entry.read()
#entry.close()
#print (inbox)
salida = ""

inbox = "cx kuyxnkfu úrj hcxujxqx hxlx jc qbx qj cx pdáx qj odókjlud ju hrjócx jc yjcdü árlskacxod mkuqt sdábx újckü sxlqkccd z ikík srxuqd cx skovjex pdsxóx jc nxñdúfu qjplwn qjc hxcjuérj qj hxgx qj cdn wuojcjn sdu xrpdlküxskfu qjc áxlknsxc qjc jgjlskpd qj cx uxskfu sdu jc úku qj ljsrhjlxl cx hcxüx qj cdn ukedn"

for letter in range(0,(len(inbox))):
	letra = inbox[letter]
	if chr(32) != letra:
		salida += (key.cifrado[letra])
	else:
		salida += (" ")

print (salida)
	
#que esta pasando
