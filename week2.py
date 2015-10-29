import re

text = open('sample.txt')
number_buffer = list()
for line in text:
    line = line.rstrip()
    number_in_line = re.findall('[0-9]+',line)
    if len(number_in_line)>0:
        number_buffer.append(number_in_line)

results = 0
for i in number_buffer:
    #print i
    buf = map(int,i)
    #print sum(buf)
    results = results+ sum(buf)
    
print results
    