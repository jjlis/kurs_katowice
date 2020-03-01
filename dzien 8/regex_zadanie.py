import re

pattern = re.compile(" \d\d-\d\d\d ")
pattern2 = re.compile("[\w-]+@\w+(\. \w+)+")
pattern3 = re.compile(" \d{2} \w{3} \d{4} ")

with open("input.txt", encoding= "utf-8")as text:

print(wyniki, pattern.findall(text)
print(wyniki2,pattern2.findall(text)
print(wyniki3, pattern3.findall(text)