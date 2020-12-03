import re
def match(text):
    word='ab'
    if re.search(word,text):
        return 'found a match'
    else:
        return 'not found'
print(match("i play badminton"))
print(match("abdul"))
import re
results = re.finditer(r"([0-9]{1,3)","exercise numers are 1,12,13,345")
print("number of length 1 to 3")
for n in results:
    print(n.group(0))
import re
def text_match(text1):
    pattern = '[A-Z]'
    if re.search(pattern,text1):
        return 'found'
    else:
        return 'not found'
print(text_match("The inseparables"))
import re
def char(string):
    charre = re.compile(r'[^a-zA-Z0-9]')
    string = charre.search(string)
    return not bool(string)
print(char("12344"))