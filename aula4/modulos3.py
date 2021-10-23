import re

pattern = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")

match = pattern.match("192.168.300.1")

if match is not None:
    print(match[0])

else:
    print("errou!!")
