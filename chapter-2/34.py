def word_frequency(words):
    frequency = {}
    for w in words:
        frequency[w] = frequency.get(w, 0) + 1
    return frequency
def read_words(filename):
    return open(filename).read().split()
def main(filename):
    frequency = word_frequency(read_words(filename))
    s = sorted(frequency.items(),key=operator.itemgetter(1),reverse=True)
    for i in s:
        print i[0],": ",i[1]
if __name__ == "__main__":
    import sys
    import operator
    main(sys.argv[1])
