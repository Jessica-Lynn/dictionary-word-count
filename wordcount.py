file_open = open('test.txt') 

def count_words(filename):

    word_counts = {}

    #line = filename.rstrip()
    #line_splt = filename.split(' ')

    for line in filename:
        line = line.strip('\n')
        
        line = line.split(' ')
        for word in line:
            word = word.lower()
            word = word.strip('?')
            word = word.strip('.')
            word = word.strip(',')
        
            word_counts[word] = word_counts.get(word, 0) + 1

    return sorted(word_counts)
    #return max(word_counts)

print(count_words(open('test.txt')))