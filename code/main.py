import Tokenizer
import dataProcesser
import W2v
import eda


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
    text = 'བཀྲ་ཤིས་བདེ་ལེགས་ཞུས་རྒྱུ་ཡིན་ སེམས་པ་སྐྱིད་པོ་འདུག།'
    outputModel = 'models/segedCorpus.model'
    model = W2v.load_word2vec_model(outputModel)

    print(text, '\n')
    print('\n'.join(eda.EDA(text, model, 15, 0.5, 0.5, 0.5, 0.5)))
    
    pass


if __name__ == '__main__':
    # pre_process()
    main()