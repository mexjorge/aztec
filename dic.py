f=open('datos.txt')
dic=[]

for linea in f.readlines():
	l=linea.rstrip("\n").split(' ')
	for palabra in l:
		if palabra not in dic:
			dic.append(palabra)

print dic
