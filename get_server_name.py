import urllib2


site =raw_input('enter site whose server u waane find= ')
p=urllib2.urlopen("http://"+site)
print p.headers.items()

#find server name from headers
'''from the info you are left with see for term server you will easily
 be able to see server name of site your site using '''
