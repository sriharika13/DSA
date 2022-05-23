#This is an Encryption and Decryption Question.

'''You get a String as an input from the user, encrypt and decrypt the string and give a final output of 3 lines:

String by User
Encrypted String
Decrypted String

Encryption Rules:

Vowels to be returned as UpperCase
Consonants to be return with 3 places shifted among consonants ONLY
Remaining All special characters will be same
Decryption Rules:

This will be the opposite of Encryption Rules.''''


def encrDecr( s:str):
    vowels=['a', 'e', 'i', 'o', 'u']
    def encr(s):
        encr_str=''
        for ch in s:
            if ch in vowels:
                encr_str+=ch.upper()
                # print(encr_str)
            elif ord(ch) in range(97, 123):
                v_cnt=0 #check for vowels while shifting consonants
                if ch=='x':
                    encr_str+='b'
                elif ch=='y':
                    encr_str+='c'
                elif ch=='z':
                    encr_str+='d'
                else:
                    for i in range(1,4):
                        if(chr(ord(ch)+i) in vowels ):
                            v_cnt+=1
                    encr_str+= chr((ord(ch)+3+ v_cnt))
            else:
                encr_str+=ch
        return encr_str
        
        # decrypting function:
    def decr(encr_str):
        s=encr_str
        decr_str=''
        for ch in s:
            if ch.isupper():
                decr_str+=ch.lower()
                # print(decr_str)
            elif ord(ch) in range(97, 123):
                v_cnt=0 #check for vowels while shifting consonants
                if ch=='b':
                    decr_str+='x'
                elif ch=='c':
                    decr_str+='y'
                elif ch=='d':
                    decr_str+='z'
                else:
                    for i in range(1,4):
                        if(chr(ord(ch)-i) in vowels ):
                            v_cnt+=1
                    decr_str+= chr((ord(ch)-3- v_cnt))
            else:
                decr_str+=ch
        return decr_str
        
    # printing output:
    print(s)
    encr_result=encr(s)
    print(encr_result)
    decr_result=decr(encr_result)
    return decr_result
  
# EXAMPLE TO SHOW USER INPUT-
# r=encrDecr("zero point")
# print(r)        
