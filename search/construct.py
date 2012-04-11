from re import sub

def parse_words(doc, content):

    # split and keep the words
    words = [x.lower() for x in sub(r'\W', ' ', content).split() if len(x) > 2]
    print str(words) 