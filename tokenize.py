import numpy as np
from string_examples import *

def find_most(s_ids):
    # Need to iterate through strings of all length
    # and then find which occurs the most
    stats = {}
    for i, j in zip(s_ids,s_ids[1:]):
        stats[(i,j)] = stats.get((i,j),0) + 1    
    top_most = max(stats,key=stats.get) # Without the stats.get, the max will be based on keys
    return top_most

def replace(tokens,vocab_size = 255):    
    pair = find_most(tokens)
    newlist = []
    i = 0
    while i < len(tokens):
        if i < len(tokens)-1 and (tokens[i], tokens[i+1]) == (pair[0], pair[1]):
            newlist.append(vocab_size + 1)         
            i += 2
        else:
            newlist.append(tokens[i])
            i += 1    
    return newlist, pair,vocab_size+1


def decode(tokens, decode_dict):    
    while True:
        flag = 1
        new_tokens = []
        for t in tokens:
            if t in decode_dict:
                new_tokens.append(decode_dict[t][0])
                new_tokens.append(decode_dict[t][1])
                # print(new_tokens)                
                flag = 0
            else:
                new_tokens.append(t)
                # print(new_tokens)
        if flag == 1:            
            break        
        tokens = new_tokens            
    return new_tokens

def encode(tokens,encode_dict):    
    new_tokens = []
    for pair in encode_dict.keys():
        i = 0
        while i < len(tokens) - 1:
            if (tokens[i], tokens[i+1]) == pair:
                new_tokens.append(encode_dict[pair])
                i += 2
            else:                
                new_tokens.append(tokens[i])
                i += 1
        new_tokens.append(tokens[i])
        tokens = new_tokens.copy()
        new_tokens = []
    return tokens


def testit(vstring,encode_dict,decode_dict):
    tokens = vstring.encode("utf-8") # in raw bytes    
    tokens = list(map(int,tokens))
    encoded = encode(tokens,encode_dict)
    decoded = decode(encoded,decode_dict)    
    byte_data = bytes(decoded)
    decoded_string = byte_data.decode('utf-8')
    return vstring == decoded_string

def learn_dict(mystring,des_size):
    tokens = mystring.encode("utf-8") # in raw bytes    
    tokens = list(map(int,tokens))
    decode_dict = {}    
    desired_vocab_size = des_size
    for vocab_size in range(255,desired_vocab_size):
        tokens, pair, id = replace(tokens,vocab_size)
        decode_dict.update({id:pair})  
    return decode_dict


if __name__ == "__main__":
    
    decode_dict = learn_dict(mystring,275)                          
    encode_dict = {pair:id for id, pair in decode_dict.items()}        
    print(testit(valstring,encode_dict,decode_dict))
        






    
