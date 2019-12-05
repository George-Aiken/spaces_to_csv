import sys
import re

#This replaces the spacing between words with commas.
#New lines are still treated as new lines.
with open(sys.argv[1]) as fp:
    line = fp.readline()
    while line:
       print(re.sub("\s+", ",", line.strip()))
       line = fp.readline()
