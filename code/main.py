import Tokenizer
import dataProcesser
import W2v


parentFolderPaths = ['corpus/classical/', 'corpus/modern/']
corpusPath = 'corpus/'
corpusFileName = 'corpus.txt'
segedCorpusFileName = 'segedCorpus.txt'
outputVector = 'models/segedCorpus.vector'
outputModel = 'models/segedCorpus.model'


def pre_process():
    dataProcesser.combine_subdir_text(corpusPath, parentFolderPaths)
    dataProcesser.combine_dir_text(corpusPath, corpusFileName)

    Tokenizer.text_tokenize(corpusPath + corpusFileName, corpusPath, segedCorpusFileName, dialect_name='general')

    W2v.train_word2vec_model(corpusPath + segedCorpusFileName, outputVector, outputModel)

    pass


def main():
    model = W2v.load_word2vec_model(outputModel)
    word = 'བུད་མེད་'
    print(word)
    similar_words = W2v.calculate_most_similar(model, word)        
    for term in similar_words:
        print(term[0], term[1])
    
    print(Tokenizer.sentence_tokenize("བཀྲ་ཤིས་བདེ་ལེགས་ཞུས་རྒྱུ་ཡིན་ སེམས་པ་སྐྱིད་པོ་འདུག།"))
    
    pass


if __name__ == '__name__':
    # pre_process()
    main()