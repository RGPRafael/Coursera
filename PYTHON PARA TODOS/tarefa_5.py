import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
uh = urllib.request.urlopen(address, context=ctx).read()
tree = ET.fromstring(uh)
results =  tree.findall('.//count')
sum = 0
for item in results:
    sum = sum + int(item.text)
print(sum)
