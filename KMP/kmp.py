import os

# Python program for KMP Algorithm
def searching():
    file = open(os.getcwd()+"/KMP/text.txt", "r")
    text = file.read().replace('\n', ' ').lower()
    N=len(text)
    file.close

    file = open(os.getcwd()+"/KMP/pattern.txt", "r")
    pattern = file.read().replace('\n', ' ')
    M=len(pattern)
    file.close
 
    phi = [0]*M
    j = 0

    processing(pattern, M, phi)
 
    i = 0
    occurrence=0

    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1
 
        if j == M:
            print ("Found pattern at ", str(i-j))
            j = phi[j-1]
            occurrence=occurrence+1
 
        elif i < N and pattern[j] != text[i]:
            if j != 0:
                j = phi[j-1]
            else:
                i += 1

    print(f"Total occurencies: {occurrence}")

def processing(pattern, M, phi):
    len = 0
    phi[0]
    i = 1

    while i < M:
        if pattern[i]== pattern[len]:
            len += 1
            phi[i] = len
            i += 1
        else:
            if len != 0:
                len = phi[len-1]
            else:
                phi[i] = 0
                i += 1

if __name__ == '__main__':
    searching()