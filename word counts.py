document = "The pen is a pen and a pencil is better than pen"
words = document.split(" ")  #creating a list of words in document
print(words)
print(type(words))
word_counts = {}

#USING for loop
for word in words :
    if word in word_counts :
        word_counts[word] += 1
    else :
        word_counts[word] = 1

print(word_counts)

#USING defaultdict() from advanced collections

from collections import  defaultdict

num_words = defaultdict(int) #creates an empty dictionary and initialises it to zero
for word in words :
    num_words[word] += 1

print(num_words)

#USING counter method from collections

from collections import  Counter  #counter counts number of times a item appears in a list

using_counter = Counter(words)
print(f"Using Counter method from collections module {using_counter}")

#printing the most frequent words in document

for word,count in using_counter.most_common(3):   # count_dict.mostcommon(n)  here count_dict is Cunter dictionary containing words and counts
    print(tuple((word,count)))