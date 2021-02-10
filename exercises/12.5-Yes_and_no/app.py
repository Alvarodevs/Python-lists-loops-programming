theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:

def wikis(ele):
    if ele == 0:
       return "woko"
    elif ele == 1:
        return "wiki"

wiki_list = list(map(wikis, theBools))

print(wiki_list)


