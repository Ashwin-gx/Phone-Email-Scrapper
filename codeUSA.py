#Phonenuber&emailscarapper
import re 
import pyperclip 
#regex for phone num
phoneregex=re.compile(r'''
(
((\d\d\d)| (\(\d\d\d\)))? #area-code
(\s|-)                    #seperator
\d\d\d                    #first3
-                         #seperator
\d\d\d\d                  #last 4 digits
)
''', re.VERBOSE)
#regex for email
emailregex= re.compile(r''' 

[a-zA-Z0-9_.+]+    # namepart
@                  # @ symbol
[a-zA-Z0-9_.+]+    # domainnamepart

''', re.VERBOSE)
#get the text of the clipboard using the pyperclip module
text = pyperclip.paste()

#Extract the email and the phno. from the copied text

extractedemail = emailregex.findall(text)
extractedphone = phoneregex.findall(text)

allphone=[]
for phoneno in extractedphone:
    allphone.append(phoneno[0])    #extracting the main phonenumber out of the unneccessary rest tupils

#Copy the extracted email/phone to the clipboard
results='\n'.join(allphone)+ '\n' + '\n'.join(extractedemail)
pyperclip.copy(results)