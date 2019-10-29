#/usr/bin/python3

from datetime import datetime
import requests as req
import sys, os, re


print('Started : '+str(datetime.today())+'\n')

try:
    os.mkdir('Emails')
except Exception as exp:
	pass

url = sys.argv[1]
res = req.get(url)

emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',res.text,re.IGNORECASE)

for email in emails:
	print(email)

domains = re.findall(r'@(\w+\.\w+)',str(emails))

dom_list = []

for domain in domains:
	if domain not in dom_list:
		dom_list.append(domain)
	else:
		pass

os.chdir('Emails')

filename = input('\nEnter filename to save : ')

with open(filename,'w') as fp:
	fp.write('Time : '+str(datetime.today()))
	fp.write('\nWeb address : '+str(res.url)+'\n\n')
	for dom in dom_list:
		fp.write('\n____'+str(dom)+'____\n\n')
		for email in emails:
		    if email.endswith(dom):
			    fp.write(email+'\n')
		    else:
			    None

print('Emails are stored in '+filename)
print('\nFinished '+str(datetime.today()))