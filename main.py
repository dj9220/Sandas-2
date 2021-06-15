# Task 2
def areDistinct(strr, i, j):
    visited = [0] * (26)

    for k in range(i, j + 1):
        if (visited[ord(strr[k]) -
                    ord('a')] == True):
            return False

        visited[ord(strr[k]) -
                ord('a')] = True

    return True

def get_word_length(word):
    res = 0
    for i in range(len(word)):
        for j in range(i,len(word)):
            if(areDistinct(word,i,j)):
                res = max(res, j-i+1)
    print(res)
if __name__ == '_main_':
    s = input('Enter word: ')
    get_word_length(s)