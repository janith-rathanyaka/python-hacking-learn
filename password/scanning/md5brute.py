#!/usr/bin/python


import hashlib

def tryOpen(wordlist):
    global pass_file
    try:
          pass_file = open(wordlist,"r")
    except:
          print("[!!] No Such File At That Path! ")
          quit()

pass_hash = input("[!!] Enter MD5 Hash Value ")
wordlist = input("[*] Enter Path To The Password File ")
tryOpen(wordlist)

for word in pass_file:
      print("[.] Trying: " + word.strip("\n"))
      enc_wrd = word.encode('utf-8')
      md5digest = hashlib.md5(enc_wrd.strip()).hexdigest()

      if md5digest == pass_hash:
          print("[+] Password Found: " + word)
          exit(0)
