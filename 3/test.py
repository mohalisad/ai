import nltk

def filter(inp):
    wnl = nltk.stem.wordnet.WordNetLemmatizer()
    stop_words = set(nltk.corpus.stopwords.words('english'))
    tokenizer = nltk.tokenize.RegexpTokenizer('\w+')

    tokens = tokenizer.tokenize(inp)
    tokens = [token.lower() for token in tokens]

    filtered = []
    for token,pos in nltk.pos_tag(tokens):
        if token not in stop_words:
            pos = pos[0].lower()
            if pos in ['a','n','v']:
                filtered.append(wnl.lemmatize(token,pos))
            else:
                filtered.append(wnl.lemmatize(token))
    return filtered
print(filter(input()))
