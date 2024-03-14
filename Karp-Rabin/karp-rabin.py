import os
 
def searching():
    file = open(os.getcwd()+"/Karp-Rabin/text.txt", "r")
    text = file.read().replace('\n', ' ').lower()
    N=len(text)
    file.close

    sigma = ''.join(set(text))
    d = len(sigma)

    file = open(os.getcwd()+"/Karp-Rabin/pattern.txt", "r")
    pattern = file.read().replace('\n', ' ')
    M=len(pattern)
    file.close
    print(f"Pattern: {pattern}")
 
    # Prime number
    q=101

    p=0    # hash value for pattern
    t=0    # hash value for text
    h=1
    occurrence=0
 
    for i in range(M-1):
        h = (h*d) % q
 
    for i in range(M):
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q
 
    # Slide the pattern over text one by one
    for i in range(N-M+1):
        if p == t:
            for j in range(M):
                if text[i+j] != pattern[j]:
                    break
                else:
                    j += 1
 
            if j == M:
                print("Pattern found at index " + str(i))
                occurrence=occurrence+1

        if i < N-M:
            t = (d*(t-ord(text[i])*h) + ord(text[i+M])) % q
            if t < 0:
                t = t+q

    print(f"Total occurencies: {occurrence}")
 
 
if __name__ == '__main__':
    searching()
 