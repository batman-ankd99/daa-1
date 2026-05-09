import re

with open('lb-logs.log','r') as f:     #f is a pointer to file. a reference to file on disk
    data = f.read()

for line in data:      #iterating character by character, all file is a string and string is iterable
    #print(line)
    pass
#so here all data of file is being put as a string in data variable using f.read()
patt= r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})(?:\d+)?"
ip_list = []
with open('lb-logs.log','r') as f_line:
    for line in f_line:                         #line by line iteration
#        print(line)
        match = re.search(patt, line)
        if match:
            ip_list.append(match.group(1)+'.'+match.group(2)+'.'+match.group(3)+'.'+match.group(4))

#            print(match.group(0))   #group(0) means entire matched string
#            print(match.group(1))  #ye pattern total me se 1 match dega etc
#            print(match.group(2))
unique_ips = set(ip_list)
print("ips we are getting hits from : ", unique_ips)


## next how many hits from 1 ip
