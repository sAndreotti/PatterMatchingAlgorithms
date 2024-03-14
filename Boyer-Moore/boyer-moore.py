import os
NO_OF_CHARS = 256

def badCharHeuristic(string, size):
    badChar = [-1]*NO_OF_CHARS
 
    for i in range(size):
        badChar[ord(string[i])] = i
 
    return badChar

def searching():
    file = open(os.getcwd()+"/Boyer-Moore/text.txt", "r")
    text = file.read().replace('\n', ' ').lower()
    N=len(text)
    file.close

    file = open(os.getcwd()+"/Boyer-Moore/pattern.txt", "r")
    pattern = file.read().replace('\n', ' ')
    M=len(pattern)
    file.close
    print(f"Pattern: {pattern}")
 
    badChar = badCharHeuristic(pattern, M)
 
    s = 0
    occurrence=0
    while(s<=N-M):
        j=M-1
 
        while j>=0 and pattern[j]==text[s+j]:
            j=j-1

        if j<0:
            print("Pattern occur at shift = {}".format(s))
            s=s+(M-badChar[ord(text[s+M])] if s+M<N else 1)
            occurrence=occurrence+1
        else:
            s=s+max(1, j-badChar[ord(text[s+j])])
            
    print(f"Total occurencies: {occurrence}")

if __name__ == '__main__':
    searching()