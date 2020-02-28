


import sys

config_file = "config.txt"

command = "interface "

sections = ["vlan","interface","ip route", "access-list", "ip access-list", "prefix-list", "route-map"]

filenames = ["vlan.cfg","interface.cfg","iproute.cfg","acl.cfg","ipacl.cfg","preflist.cfg","routemap.cfg"]


def file_read(fn):
    """ Opens the input configuration file as inputfile"""
    with open(fn,'r') as inputfile:
        cfg = inputfile.read()
    return(cfg)


def file_create(fn, final):
    """Opens destination file and writes out the content  of the final list"""
    with open (fn,'w') as outputfile:
        for lines in final:
            outputfile.write(lines+'\n')
    return()


def route_find(section, input):
    result = []
    for element in input:
        if section in element:
            result.append(element)
    return(result)

def section_process(section, input):
    """Finds a section in each line of the input configuration file. If finds, or the consecutive lines belong
       to the same section, it puts them into the list called final"""

    l = len(section)
    result=[]
    diff = []
    final = []
    index = 0
    while index < len(input):
        if  input[index][0:l] == section:
            result.append(input[index])
            index = index+1
            while input[index] != "!":
                result.append(input[index])
                index = index+1
            result.append("!")
        index = index+1
    print("------------------")
    for element in result:
       if ((element != "!") and (element[0:l] != section) and (element[0] !=" ")):

           diff.append(element)

    for element in result:
          if element not in diff:
                final.append(element)
    return(final)

def section_create(section, name):
    result = file_read(config_file)
    result = result.split("\n")
    result = section_process(section, result)
    file_create(name,result)
    for line in result:
        print(line)





if  __name__ == "__main__":

    for section in sections:
       outfilename =  filenames[sections.index(section)]
       section_create(section, outfilename)
