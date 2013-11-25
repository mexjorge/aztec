# -*- coding: utf-8 -*-
def Anagramas(words, filter): 
  a = {} 
  for w in words: 
    k = ''.join(sorted(filter(w))) 
    if not k in a: 
      a[k] = [] 
    a[k].append(w) 
  return a 
 
 
 
 
 
# == usage ======================================================== 
import sys 
import string 
import unicodedata 
 
for k, v in Anagramas(map(string.rstrip, sys.stdin.readlines()), 
                      # filtro de caracteres, aquí se considera 'n' == 'ñ', 'A' == 'ä', etc... 
                      lambda c: unicodedata.normalize('NFD', c.decode('utf-8', 'ignore')).encode('ascii', 'ignore').lower()).iteritems(): 
  if len(v) > 1: 
    print ', '.join(v) 