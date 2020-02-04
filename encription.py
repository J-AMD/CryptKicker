import key

#entry = open('input.txt', 'r')
#inbox = entry.read()
#entry.close()
#print (inbox)
salida = ""
keywords={}

key = "El veloz murciélago hindú comía feliz cardillo y kiwi cuando la cigüeña tocaba el saxofón detrás del palenque de paja"
inbox = "cx kuyxnkfu úrj hcxujxqx hxlx jc qbx qj cx pdáx qj odókjlud ju hrjócx jc yjcdü árlskacxod mkuqt sdábx újckü sxlqkccd z ikík srxuqd cx skovjex pdsxóx jc nxñdúfu qjplwn qjc hxcjuérj qj hxgx qj cdn wuojcjn sdu xrpdlküxskfu qjc áxlknsxc qjc jgjlskpd qj cx uxskfu sdu jc úku qj ljsrhjlxl cx hcxüx qj cdn ukedn"


key_list= key.split()

for i in key_list:
    keywords[key_list.index(i)+1]=len(i) #carga diccionaria
    
inbox_list= inbox.split()

key_index= 0
cont= 0
for i in inbox_list:
    if len(i)==keywords[key_index]:
        key_index+=1
    else:
        key=1
    cont += 1

start_position= cont - len(key_list) #posicion inicial de la llave



    






"""
for letter in range(0,(len(inbox))):
	letra = inbox[letter]
	if chr(32) != letra:
		salida += (key.cifrado[letra])
	else:
		salida += (" ")

print (salida)
""""