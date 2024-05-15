import numpy as np

def find_most(s_ids):
    # Need to iterate through strings of all length
    # and then find which occurs the most
    stats = {}
    for i, j in zip(s_ids,s_ids[1:]):
        stats[(i,j)] = stats.get((i,j),0) + 1    
    top_most = max(stats,key=stats.get) # Without the stats.get, the max will be based on keys
    return top_most

def bpe(s):
    vocab_size = 255    
    pair = find_most(tokens)
    newlist = []
    i = 0
    while i < len(tokens)-1:
        if (tokens[i], tokens[i+1]) == (pair[0], pair[1]):
            newlist.append(vocab_size+1)
            i += 2
        else:
            newlist.append(tokens[i])
            i += 1
    newlist.append(tokens[i])             
    return newlist


if __name__ == "__main__":
    mystring = "I would like to order a Pizza. I like Pizzas"
    tokens = mystring.encode("utf-8") # in raw bytes    
    tokens = list(map(int,tokens))
    print(tokens)
    print(bpe(tokens))
    
