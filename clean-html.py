#!/usr/bin/python3
import sys
import os.path

from bs4 import BeautifulSoup


if len(sys.argv) != 2:
    sys.stderr.write("Usage %s <filename>\n"%(sys.argv[0]))
    sys.exit(1)

filename = sys.argv[1]

if not os.path.isfile(filename):
    sys.stderr.write("File [%s] did not exist\n"%(filename))
    sys.stderr.write("Usage %s <filename>\n"%(sys.argv[0]))
    sys.exit(1)

html = open(filename).read()
soup = BeautifulSoup(html,'html.parser')


# replace with `soup.findAll` if you are using BeautifulSoup3
for rt in soup.find_all("rt"): 
    rt.decompose()
for ruby in soup.find_all("ruby"): 
    ruby.unwrap()

for p in soup.find_all("p"): 
    print(p.get_text())




