import os

def preprocessing():
    file = open(os.getcwd()+"/KMP/pattern.txt", "r")
    pattern = file.read().replace('\n', ' ')
    file.close()

    print(f"Pattern: {pattern}")
    M=len(pattern)

    index = int(0)
    phi = list()
    while(index<M):
        if index>=1 and index<=M:
            phi.insert(index,len(border(pattern[:index+1])))
        else:
            phi.insert(index, -1)

        index = index+1
    
    print(phi)
    return phi

def searching():
    file = open(os.getcwd()+"/KMP/text.txt", "r")
    text = file.read().replace('\n', ' ').lower()
    N=len(text)
    file.close

    file = open(os.getcwd()+"/KMP/pattern.txt", "r")
    pattern = file.read().replace('\n', ' ')
    M=len(pattern)
    file.close

    phi = preprocessing()
    j=0

    for q in range(0, N):
        while j>=0 and pattern[j+1]!=text[q]:
            j = phi[j]
        j = j+1
        if j==M-1:
            print(f"Pattern found at {q-M+1}")
            j = phi[j]

def border(str):
    bd = ""
    for i in range(1, len(str)-1):
        if str[:i] == str[-i:]:
            bd = str[:i]

    return bd

if __name__ == '__main__':
    searching()