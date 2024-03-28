import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
from typing import TextIO
from rake_nltk import Rake

# download the necessary resources
nltk.download('punkt', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('stopwords', quiet=True)

def keywordCounter(text_file: TextIO) -> str:
    with open(text_file, 'r') as file:
        text = file.read().replace('\n', ' ')
  
    # tokenization
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())

    # removing stop words
    filtered_words = [word for word in words if word.lower() not in stop_words and word.isalnum()]

    # POS tagging
    tagged_words = nltk.pos_tag(filtered_words)

    # extracting keywords
    keywords = [word for word, tag in tagged_words if tag in ('NN', 'NNS', 'NNP', 'NNPS')]

    # counting the keywords
    keyword_counter = Counter(keywords)

    # for k,v in sorted(keyword_counter.items()):
    #     print(list(k, v))

    print(keyword_counter)



def keywordExtractorRake(text_file: TextIO) -> str:
    r= Rake()

    with open(text_file, 'r') as file:
        text = file.read().replace('\n', ' ')

    r.extract_keywords_from_text(text)

    phrases_unique = []
    phrases = r.get_ranked_phrases()
    for phrase in phrases:
        if phrase not in phrases_unique and phrase.isdigit() == False:
            phrases_unique.append(phrase.strip())

    print(phrases_unique)
    

def main():
    print("\n[ KEYWORD COUNTER ]\n")
    keywordCounter('text.txt')
    print("\n[ PHRASE EXTRACTION ]\n")
    keywordExtractorRake('text.txt')    


if __name__ == '__main__':
    main()
