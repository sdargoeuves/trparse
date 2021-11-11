import re

def extractIPs(fileContent):
    pattern = r"((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)([ (\[]?(\.|dot)[ )\]]?(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3})"
    ips = [each[0] for each in re.findall(pattern, fileContent)]
    if len(ips) >= 1:
        for item in ips:
            location = ips.index(item)
            ip = re.sub("[ ()\[\]]", "", item)
            ip = re.sub("dot", ".", ip)
            ips.remove(item)
            ips.insert(location, ip)
    else:
        ips = "*"
    return ips

ips = []
with open("path2.txt") as fp:
    for line in fp:
        ip = extractIPs(line)
        print(f"{ip}")
        ips.append(ip)
        