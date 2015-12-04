import hashlib
md5hash = hashlib.md5()
secret = "ckczppom"
number = 0
#md5hash.update("abcdef609043")
print(md5hash.hexdigest())
while md5hash.hexdigest()[0:6] != "000000":
    number += 1
    md5hash = hashlib.md5(secret + str(number))
    print(md5hash.hexdigest() + " " + str(number) + " " + secret + str(number))
print(str(number) + " hex: " + md5hash.hexdigest())
