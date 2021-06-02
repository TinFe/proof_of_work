import hashlib
import time

user_input = ''

def run_again():
    if user_input == '':
        return True

while run_again() == True:
    nonce_int = 0
    print('Type a random seed')
    seed = str(input())
    nonce_max = float('inf')
    print("minimum leading 0's?")
    lead_0_len = int(input())
    start_time = time.time()


    while nonce_int <=nonce_max:
        nonce_str = str(nonce_int)+seed
        hash_input = hashlib.sha256(nonce_str.encode('UTF-8'))
        hash_output = hash_input.hexdigest()
        if hash_output[0:lead_0_len] == str(lead_0_len*'0'):
            print('hash input:')
            print(seed+str(nonce_int))
            print('golden nonce:')
            print(nonce_int)
            print(hash_output)
            break
            
        nonce_int += 1
    
    elapsed_time = ("---- %s seconds ----" % (time.time() - start_time))
    hash_per_sec = nonce_int/(time.time() - start_time+.00000001)
    print('')
    print('total hashes:')
    print(nonce_int)
    print(elapsed_time)
    print('hashes/second')
    print(hash_per_sec)
    print("Press enter to run again (n to close)") 
    user_input += input()
