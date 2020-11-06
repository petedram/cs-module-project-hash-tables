'''
Input: a string of words separated by spaces. Only the letters `a`-`z`
are utilized.

Output: the string in the same order, but with subsequent duplicate
words removed.

There must be no extra spaces at the end of your returned string.

The solution must be `O(n)`.
'''

def no_dups(s):
    # Your code here

    #add each word to a hash table, word is the key, value is a count
    our_dict = {}

    words = s.split()
    new_string = ''
    count = 0
    for word in words:
        if word in our_dict:
            our_dict[word] +=1
            count +1
        else:
            if count == 0:
                new_string = new_string + word
                our_dict[word] = 1
                count +=1
            else:
                new_string = new_string + ' ' + word
                our_dict[word] = 1
                count +=1
    
    return (new_string)





if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))