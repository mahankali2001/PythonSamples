# 1. read every line from the file - loop
# 2. split by space and get words from each line
# 3. add each word with count to dictionary and skip the words that are not required -- loop
# 4. sort dictionary by count
# 5. print top 5 words
def topFiveWords(file):
    word_counts = {} # Create an empty dictionary to store the word counts
    word_specialCharsToStripRegex = r'[.,!?;()[]]'
    words_toskip = ['and', 'the', 'to', 'in', 'of', 'a', 'was', 'for', 'as', 'on', 'with', 'is', 'it']
    with open(file, 'r') as f:
        for line in f:
            words = line.split() # Split the line into words using the space character as the separator, store the words in a list
            words = [word.strip(word_specialCharsToStripRegex) for word in words] # Remove punctuation from each word
            for word in words:
                word = word.lower()
                if word not in words_toskip:
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1
    
    sorted_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True) # Sort the words by their counts in descending order
    
    top_five = sorted_words[:5]
    
    for word, count in top_five:
        print(f'{word}: {count}')

filename = 'data/photoshop.txt'
topFiveWords(filename)


# for key in word_counts:
#     print(key)

# for value in word_counts.values():
#     print(value)

# for key, value in word_counts.items():
#     print(f'{key}: {value}')




# def topFiveWords(file):
#     df = pd.read_csv(file, header=None, names=['text']) # Read the text file into a DataFrame with a single column 'text' and no header row 
#     word_counts = {}
    
#     for line in df['text']:
#         words = line.split()
#         for word in words:
#             word = word.lower()
#             if word in word_counts:
#                 word_counts[word] += 1
#             else:
#                 word_counts[word] = 1
    
#     print(word_counts)
#     sorted_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True) # Sort the words by their counts in descending order
#     top_five = sorted_words[:5]
    
#     for word, count in top_five:
#         print(f'{word}: {count}')

# filename = 'data/photoshop.txt'
# topFiveWords(filename)