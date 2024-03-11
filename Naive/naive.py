import os

def searching():
    file = open(os.getcwd()+"/Naive/text.txt", "r")
    text = file.read().replace('\n', ' ').lower()
    N=len(text)
    file.close

    file = open(os.getcwd()+"/Naive/pattern.txt", "r")
    pattern = file.read().replace('\n', ' ')
    M=len(pattern)
    file.close
    print(f"Pattern: {pattern}")

    occurrence=0
    
    for i in range(N - M + 1):
        j = 0
 
        while(j < M):
            if (text[i + j] != pattern[j]):
                break
            j += 1
 
        if (j == M):
            print("Pattern found at index ", i)
            occurrence=occurrence+1

    print(f"Total occurencies: {occurrence}")

if __name__ == '__main__':
    searching()