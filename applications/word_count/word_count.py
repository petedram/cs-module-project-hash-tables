'''
count the words in an input string:
Hello, my cat. And my cat doesn't say "hello" back.

It returns a dictionary of words and their counts:
{'hello': 2, 'my': 2, 'cat': 2, 'and': 1, "doesn't": 1, 'say': 1, 'back': 1}

case ignored, output lower case
Key order in the dictionary doesn't matter.

Split the strings into words on any whitespace.

Ignore each of the following characters:

```
" : ; , . - + = / \ | [ ] { } ( ) * ^ &
```

If the input is empty or contains only ignored characters, return an empty dictionary.

'''
#s = a single string

def word_count(s):
    # Your code here

    #remove ignored 
    ignore_list = set('":;,.-+=/\|[]{}()*^&')
    unignored = ''
    for letter in s:
        if letter in ignore_list:
            pass
        else:
            unignored = unignored + letter.lower()
    
    #check not empty
    if unignored == '':
        return {}
    
    print(unignored)
    res = unignored.split()


    # dict_res = {}

    our_dict = {}

    for word in res:
        if word in our_dict:
            our_dict[word] +=1
        else:
            our_dict[word] = 1

    return (our_dict)


    # for word in res:
    #     word_store.put(word,1)

    # print(f'load is {word_store.load}')



    # for item in word_store.data:
    #     if item != None:
    #         print(item.key, item.load)
    #         if item.next != None:
    #             print(item.next.value)



# word_count('Hello, my cat. And my cat doesn\'t say "hello" back.')



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))