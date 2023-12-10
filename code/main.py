import Tokenizer
import dataProcesser
import W2v

def pre_process():
    parentFolderPaths = ['corpus/classical/', 'corpus/modern/']
    corpusPath = 'corpus/'
    corpusFileName = 'corpus.txt'
    dataProcesser.combine_subdir_text(corpusPath, parentFolderPaths)
    dataProcesser.combine_dir_text(corpusPath, corpusFileName)

    segedCorpusFileName = 'segedCorpus.txt'
    Tokenizer.tibetanTokenize(corpusPath + corpusFileName, corpusPath, segedCorpusFileName, dialect_name='general')

    outputVector = 'models/segedCorpus.vector'
    outputModel = 'models/segedCorpus.model'
    W2v.train_word2vec_model(corpusPath + segedCorpusFileName, outputVector, outputModel)

    pass


def main():
    model = W2v.load_word2vec_model(outputModel)
    word = 'བུད་མེད་'
    print(word)
    similar_words = W2v.calculate_most_similar(model, word)        
    for term in similar_words:
        print(term[0], term[1])
    
    pass


if __name__ == '__name__':
    main()