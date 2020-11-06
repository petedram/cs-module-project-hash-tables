import random

# Read in all the words in one go
with open("/Users/petejames/lambda-cs/cs-module-project-hash-tables/applications/markov/input.txt") as f:
    words = f.read()

# f = open('input.txt', 'r')
# words = f.read()

# TODO: analyze which words can follow other words
# Your code here
words_list = words.split()
our_dict = {}
index_count = 0

# Start words are words that begin with a capital, or a `"` followed by a
# capital.
def check_start(word):
    if word[0].isupper():
        return True
    
    elif word[0] == '"' and word[1].isupper():
        return True
    
    else:
        return False

# Stop words are words that end in any of the punctuation `.?!`, or that
# punctuation followed by a `"`.
def check_end(word):
    end_list = set('.?!')
    if word[len(word)-1] in end_list:
        return True
    
    elif word[len(word)-1] == '"' and word[len(word)-2] in end_list:
        return True
    
    else:
        return False


for word in words_list:
    if index_count +1 == len(words_list):
        rando_sentence = ''
        #select a random word from words_list to start with
        current_word = random.choice(words_list)

        #while loop to select a start word
        while check_start(current_word) == False:
            #random until it is start word
            current_word = random.choice(words_list)

        rando_sentence = current_word

        #set a next word
        next_word = random.choice(our_dict[current_word])
        rando_sentence = rando_sentence + ' ' + next_word

        #while next_word is not a stop_word:
        while check_end(next_word) == False:
            #set next word to a random word in the current word dictionary 
            next_word = random.choice(our_dict[next_word])
            rando_sentence = rando_sentence + ' ' + next_word

        print(rando_sentence)
        break

    #get next word via index count
    next_word = words_list[index_count + 1]

    #check if new word for dictionary
    if word not in our_dict:
        #create new list containing next word
        our_dict[word] = [next_word]
    else:
        #append next word to the list
        our_dict[word].append(next_word)
    
    index_count +=1
    


    



# TODO: construct 5 random sentences
# Your code here

