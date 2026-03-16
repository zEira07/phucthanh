def word_frequency(text):
    words = text.lower().split()
    
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    # sort dictionary by frequency
    sorted_words = sorted(freq.items(), key=lambda item: item[1], reverse=True)

    # get top 5
    top5 = dict(sorted_words[:5])

    total_words = len(words)
    top5_sum = sum(top5.values())

    proportion = (top5_sum / total_words) * 100

    print("Top 5:", top5)
    print("Total number of words:", total_words)
    print("Proportion of 5 most common words:", round(proportion, 2), "%")


# test
text = input("Enter text: ")
word_frequency(text)