import Tokenizer
import dataProcesser
import W2v
import eda
import io
from tqdm import tqdm


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
    # text = 'བཀྲ་ཤིས་བདེ་ལེགས་ཞུས་རྒྱུ་ཡིན་ སེམས་པ་སྐྱིད་པོ་འདུག།'
    outputModel = 'models/segedCorpus.model'
    model = W2v.load_word2vec_model(outputModel)
    trainset_path = 'corpus/sst2_train_500_zh_bo.txt'

    with io.open(trainset_path.rstrip('.txt') + '_augmented_5.txt', 'w+', encoding='utf-8') as f:
        for line in tqdm(open(trainset_path, encoding='utf-8')):
            augedText = []
            label, text = line.rstrip('\n').split('\t')
            augedText = eda.EDA(text, model, 5, 0.1, 0.1, 0.1, 0.1)
            for i in range(len(augedText)):
                augedText[i] = label + '\t' + augedText[i]
            augedText.append(label + '\t' + ' '.join(Tokenizer.sentence_tokenize(text.rstrip('\n'))))

            f.write('\n'.join(augedText))
            f.write('\n')
    
    pass


if __name__ == '__main__':
    # pre_process()
    main()