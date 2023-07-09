import os
import PyPDF2

print("welcome")
string2 = "http/Text to speech"

result2 = ""

for char in string2:
    if char.isupper() or char.islower() or char.isdigit() or char=='.':
        result2 += char
    else:
        result2 += " "
result2=result2[7:]
print(result2)