import re

# p=re.compile(r'\bclass')
# m=p.search('aljfkjs         classajalkjdl')
# print(m)

# p = re.compile('(ABC)+')
# m = p.search('ABCABCABC OK?')
# print(m)
# print(m.group())

# p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
# m = p.search("park 010-1234-1234 kim 010-8989-6363")
# print(m.group(0))


# p = re.compile(r'(\s+\w+\s+)')
# m=p.search('Paris in the the spring')
# print(m.group(0))


# p = re.compile(r'(\b\w+)\s+\1')
# print(p.search('Paris in the the spring').group())

# p = re.compile(r'(\b\w+\b)\s+\1')
# print(p.search('Paris in the the spring').group())

# p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
# print((p.search('Paris in the the spring')).group())

# p = re.compile(r".+:")
# m = p.search("http://google.com")
# print(m.group())

# regular expression , Lookahead Assertions, 전방탐색, forward search

# p=re.compile(r'\w+')
# m=p.search('A1 B2 c3 d_4 e:5 ffGG77--__--')
# print(m)

def hexrepl(match):
     print(match.group())
     value = int(match.group())
     return hex(value)

p = re.compile(r'\d+')
print(p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.'))
