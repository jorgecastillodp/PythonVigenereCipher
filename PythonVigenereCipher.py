import base64
from itertools import cycle



key="MOEBIUS" #str
Bkey = bytes(key, 'utf-8')
Decode=
"""DiArJTs0JzgjJDYgOj0+Y2U7JiBzPiApNCwxczknIGIrOj04PGUzPDAgOSYqLGhfWW1vZW
JpdXNtb2ViaXVzbW9lYml1c21vZWJpdXNtb2ViaXVzY2hibEN1c21vZWJpe3RqYWViaXVz
bWFlYml1c21vZWhucnltb2VicwoPYhB/Yml1c21hT2JpdXNtb38dFXoMd29lYhYJe2IQZW
Jnb31nEBltFn9zbW9/YmYJc3dvZWxue2ljaGtIaXV9amhreGl6D211ZWJpe3xkE2ViaXJp
amVlbRV1eW11ZWJue31qYWViZGhpInV4b0N1aRITah1zcn13dX9saXVzbWhlaG5yeW1vZW
JjdXRjaGpsbnUMEWdqHW57dHdoa2VDdWltYBlic3Vpd3V/eGl1c21vbx0Vegxnb2ViaXV+
cG8qYnR4c21gbB5pdXNtaE9iaXJ9Y2hlYm5vaXdoZWJpdXNnb2oeaX9zbW9lYmdyfGNoa2
JpdXRHb2ViaXVzbW9lYml1c21vZWJpdXljYW9iaXVzbW9lYmlvWQ=="""
decodeString = base64.b64decode(Decode); #byte
print(''.join(chr(x) for x in [a ^ b for a,b in zip(decodeString,cycle(Bkey))]))
