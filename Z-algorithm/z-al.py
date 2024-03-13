import os

def preprocessing(str, z):
    N=len(str)

    left,right,k=0,0,0
    for i in range(1,N):
        if i>right:
            left=i
            right=i
            while right<N and str[right-left]==str[right]:
                right=right+1
            z[i]=right-left
            right=right-1
        else:
            k=i-left
            if z[k]<right-i+1:
                z[i]=z[k]
            else:
                left=i
                while right<N and str[right-left]==str[right]:
                    right=right+1
                z[i]=right-left
                right=right-1



def searching():
    file = open(os.getcwd()+"/Z-algorithm/text.txt", "r")
    text = file.read().replace('\n', ' ').lower()
    file.close

    file = open(os.getcwd()+"/Z-algorithm/pattern.txt", "r")
    pattern = file.read().replace('\n', ' ')
    file.close

    concat=pattern+"$"+text
    z=[0]*len(concat)
    preprocessing(concat, z)
    occurrence=0

    for i in range(len(concat)):
        if z[i]==len(pattern):
            print(f"Pattern found at {i-len(pattern)-1}")
            occurrence=occurrence+1

    print(f"Total occurencies: {occurrence}")


if __name__ == '__main__':
    searching()