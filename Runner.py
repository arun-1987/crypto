from Alice import Alice
from Bob import Bob
from Message import Message


#creating alice public and private keys
aliceobject = Alice()
aprivatekey = aliceobject.create_privateKey()
apublickey = aliceobject.create_publicKey(aprivatekey)


#creating bob public and private keys
bobobject = Bob()
bobprivatekey = bobobject.create_privateKey()
bobpublickey = bobobject.create_publicKey(bobprivatekey)

#sign message using alice private key
message = b'hi i am alice'
print(f'Original message..{message}')
signature = aliceobject.sign(aprivatekey,message)

#encrypt using bob public key
encrypmessage = aliceobject.encryptmessage(bobpublickey,message)
print(f'after encryption.. {encrypmessage}')

#send to bob
messageobj = Message()
messageobj.send_message(apublickey,encrypmessage,signature)

#decrypt message
decryptedmessage = bobobject.decryptmessage(messageobj.get_message(),bobprivatekey)
print(f'After decryption..{decryptedmessage}')

#retrive original message
bobobject.verifySender(messageobj.get_public_key(),messageobj.get_signature(),decryptedmessage)
print('Verified the sender successfully..')




