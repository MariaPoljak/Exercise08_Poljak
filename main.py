import spacy
nlp = spacy.load('en_core_web_sm')

#write_to_file(text, output_file_path)

def write_to_file(text, output_file_path):
    for text in file:
        open("output_file_path", "x")
        file.write(text)
    if os.path.exists(output_file_path) == True:
        raise RuntimeError("Output file already exists!")

#count_stopwords(input_file_path)

spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
len(spacy_stopwords)

def count_stopwords(input_file_path):
    stopwords = spacy_stopwords
    input_file_path = fileinput
    for stopwords in input_file_path:
        print(len(spacy_stopwords)) in open('stopwords_count.txt', 'x')
    if len(spacy_stopwords) == 0:
        return 0


#remove_stopwords(input_file_path, output_file_path)

def remove_stopwords(input_file_path, output_file_path):
    my_doc = input_file_path
    new_doc = output_file_path
    included_stopwords = []
    for word in my_doc:
        if word in spacy_stopwords:
            included_stopwords.append(word)
    return included_stopwords in open('removed_stopwords', 'x')


#tokenize_text(input_file_path, output_file_path)

def tokenize_text(input_file_path, output_file_path):
    input_file_path = nlp(input_file_path)
    output_file_path = open("tokenized_text.txt", "x")
    for token in input_file_path:
        print(f"{token.text:{15}}{token.pos_:{15}}{token.dep_:{15}}") in output_file_path