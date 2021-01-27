#!/usr/bin/python
#
# urlEncDec.py
#
# script to encode or decode a url string
#
# d3adlyv3n0m 
# https://github.com/d3adlyv3n0m/URLEncoderDecoder/blob/master/urlEncDec.py
# 
# Edited by welpxd
# Instead of https://www.urldecoder.org/ or https://www.urlencoder.org/
#########################################


import re
import os
import sys
import time
import urllib.request, urllib.parse, urllib.error
import pyperclip


def addToClipBoard(text):
    #command = 'echo ' + text.strip() + '| clip'
    command = 'echo ' +  '| clip'
    os.system(command)

# banner
# os.system('clear')
name = 'Created by ' +  ' Welpxd    ' 
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


# http://aupac.lib.athabascau.ca:4550/showres?url=http%3A%2F%2F0-www.crossref.org.aupac.lib.athabascau.ca%2Fopenurl%3Fpid%3Dath%3Aath1121%26aulast%3DGreitemeyer%26issn%3D01461672%26volume%3D40%26issue%3D5%26spage%3D578%26date%3D2014&linkid=1770053
# https://stackoverflow.com/a/20821822
# https://stackoverflow.com/a/11063483 -> pip install pyperclip


# https://github.com/jdorris61/URL-Encoder-Decoder/blob/master/EncDec.py
# https://github.com/cym13/urldecode/blob/master/urldecode.py