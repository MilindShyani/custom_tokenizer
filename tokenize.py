import numpy as np

def find_most(s_ids):
    # Need to iterate through strings of all length
    # and then find which occurs the most
    stats = {}
    for i, j in zip(s_ids,s_ids[1:]):
        stats[(i,j)] = stats.get((i,j),0) + 1    
    top_most = max(stats,key=stats.get) # Without the stats.get, the max will be based on keys
    return top_most

def replace(s,vocab_size = 255):    
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
                print("yp",i)
                new_tokens.append(encode_dict[pair])
                i += 2
            else:                
                new_tokens.append(tokens[i])
                i += 1
        new_tokens.append(tokens[i])
        tokens = new_tokens.copy()
        new_tokens = []
    return tokens


if __name__ == "__main__":
    mystring ='''
Paul Adrien Maurice Dirac OM FRS[6] (/dɪˈræk/; 8 August 1902 – 20 October 1984) was an English mathematical and theoretical physicist who is considered to be one of the founders of quantum mechanics and quantum electrodynamics.[7][8] He is credited with laying the foundations of quantum field theory.[9][10][11][12] He was the Lucasian Professor of Mathematics at the University of Cambridge, a professor of physics at Florida State University and the University of Miami, and a 1933 Nobel Prize in Physics recipient.

Dirac graduated from the Universty of Bristol with a first class honours Bachelor of Science degree in electrical engineering in 1921, and graduated from the University of Cambridge with a PhD in physics in 1926, writing the first ever thesis on quantum mechanics.[8][13]

Dirac made fundamental contributions to the early development of both quantum mechanics and quantum electrodynamics, coining the latter term.[11] Among other discoveries, he formulated the Dirac equation in 1928, which describes the behaviour of fermions and predicted the existence of antimatter,[14] and is considered one of the most important equations in physics,[9] with it being considered by some to be the "real seed of modern physics".[15] He wrote a famous paper in 1931,[16] which further predicted the existence of antimatter.[17][18][14] Dirac shared the 1933 Nobel Prize in Physics with Erwin Schrödinger "for the discovery of new productive forms of atomic theory".[19] He was the youngest ever theoretician to win the prize until T. D. Lee in 1957.[20] He also made significant contributions to the reconciliation of general relativity with quantum mechanics. His 1930 monograph, The Principles of Quantum Mechanics, is considered to be one of the most influential texts on quantum mechanics.[21]

Dirac's contributions were not only restricted to quantum mechanics. He contributed to the Tube Alloys project, the British programme to research and construct atomic bombs during World War II.[22][23] Furthermore, Dirac made fundamental contributions to the process of uranium enrichment and the gas centrifuge,[24][25][26][23] and whose work was deemed to be "probably the most important theoretical result in centrifuge technology".[27] He also contributed to cosmology, putting forth his large numbers hypothesis.[24][28][29][30][31] Dirac is also seen as having anticipated string theory well before its inception, with his work on the Dirac membrane and Dirac–Born–Infeld action, amongst other contributions.[32][33]
'''
    tokens = mystring.encode("utf-8") # in raw bytes    
    tokens = list(map(int,tokens))
    old_tokens = tokens.copy()
    print(len(tokens))
    decode_dict = {}    
    desired_vocab_size = 275
    for vocab_size in range(255,desired_vocab_size):
        tokens, pair, id = replace(tokens,vocab_size)
        decode_dict.update({id:pair})        
    print(len(tokens),len(old_tokens))
    encode_dict = {pair:id for id, pair in decode_dict.items()}
    print(encode_dict)
    encoded = encode(old_tokens,encode_dict)
    decoded = decode(encoded,decode_dict)    
    byte_data = bytes(decoded)
    decoded_string = byte_data.decode('utf-8')
    print(decoded_string)






    
