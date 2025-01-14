# def isPhoneNumber(text):
#     if len(text) != 12:
#        return False
#     for i in range(0, 3):
#        if not text[i].isdecimal():
#             return False
#     if text[3] != '-':
#        return False
#        for i in range(4, 7):
#            if not text[i].isdecimal():
#               return False
#     if text[7] != '-':
#        return False
#        for i in range(8, 12):
#           if not text[i].isdecimal():
#               return False
#     return True
# print('415-555-4242 is a phone number:')
# print(isPhoneNumber('415-555-4242'))
# print('Moshi moshi is a phone number:')
# isPhoneNumber("xyz xxz")

# write program to finding a pattern of the text with the regular expression
import re
phoneNumberRegex=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo=phoneNumberRegex.search("my number is 415-555-4292")
print(mo.group(0))
print(mo.group(1))
print(mo.groups())