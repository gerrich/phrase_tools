#!/usr/bin/env python

import md5
import sys

def md5hex(str):
  m = md5.new()
  m.update(str)
  return m.hexdigest()

if __name__ == "__main__":
  for phrase in sys.stdin:
    line = phrase.rstrip('\r\n')
    print [line], md5hex(line)
