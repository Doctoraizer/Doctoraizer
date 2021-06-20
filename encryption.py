from Crypto.Cipher import AES
from Crypto import Random
import base64


def encrypt_blocks(name,age,Chronic_diseases,gender,blood_type,date):
    info=[]
    encrypt_info=[]
    age=str(age)
    info=info +[name,age,Chronic_diseases,gender,blood_type,date]
    padding="*"
    block_size= 16
    key=Random.new().read(16)
    iv=Random.new().read(16)
    print(iv)
    print(len(iv))
    for i in info:
        q=lambda a : a + (block_size - len(a) %block_size)*padding
        E=AES.new(key,AES.MODE_CBC,iv)
        ciphertext=base64.b64encode(iv+E.encrypt(q(i).encode('ascii')))
        encrypt_info.append(ciphertext)
    return [encrypt_info,key]
    
     


def decrypt_blocks(encrypt_info,key):
    decrypt_info=[]
    for i in encrypt_info:
        iv=base64.b64decode(i)[:16]
        i_e=base64.b64decode(i)[16:]
        d=AES.new(key,AES.MODE_CBC,iv)
        decrypt_i=d.decrypt(i_e).decode('ascii')
        d_i=decrypt_i.rstrip("*")
        decrypt_info.append(d_i)
    decrypt_info[1]=int(decrypt_info[1])
    return decrypt_info
  



def encrypt_image(image):
    pass
def decrypt_image(image):
    pass

   


if __name__ == "__main__":
    a = encrypt_blocks('Noura',25,'None','female', 'A+','9/6/2021')
    print(a)
    print(decrypt_blocks(a[0],a[1]))
