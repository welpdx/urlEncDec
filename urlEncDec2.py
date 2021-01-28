#!/usr/bin/python
#
# urlEncDec.py
#
# script to encode or decode a url string
#
# Forked from:
# d3adlyv3n0m
# https://github.com/d3adlyv3n0m/URLEncoderDecoder/blob/master/urlEncDec.py
#
# Edited by welpxd
#
#########################################


import re
import os
import sys
import time
import urllib.request, urllib.parse, urllib.error
import pyperclip


def addToClipBoard(text):
    command = 'echo ' +  '| clip'
    os.system(command)


name = 'Modified by ' +  ' Welpxd    '
print('#################################')
print('#                               #')
print('#  ' + name + '       #')
print('#                               #')
print('#################################')
print()
time.sleep(1)

# retrieve the url string
print('[*] Enter the URL')
url = input('>>> ')

# make sure something was entered
if not url:
    print('[!] WARNING: Must enter a URL.')
    sys.exit(1)

# determine if url needs to be encoded (no hex characters)
# or decoded (contains hex characters)
hxChars = re.findall(r'\%..', url)
if hxChars:
    decUrl = urllib.parse.unquote(url)
    print('[+] Decoded URL')
    print('>>> ' + decUrl)
    pyperclip.copy(decUrl)
    spam = pyperclip.paste()
else:
    encUrl = urllib.parse.quote_plus(url)
    print('[+] Encoded URL')
    print('>>> ' + encUrl)
    #addToClipBoard(encUrl)
    pyperclip.copy(encUrl)
    spam = pyperclip.paste()

# done
sys.exit(0)
