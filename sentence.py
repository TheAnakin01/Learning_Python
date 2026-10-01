def main():
    sentence = input("Input: ")
    count = get_times(sentence)
    for word in count:
        print(f"{word}: {count[word]}")
    

def get_times(sentence):
    counts = {}
    for word in sentence.split():
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
   
if __name__ == "__main__":
    main()