'''
对藏语分词工具botok进行调试
'''
from botok import WordTokenizer
from botok.config import Config
from pathlib import Path
import io
import os

def sentence_tokenize(text , dialect_name='general'):
    config = Config(dialect_name=dialect_name)
    wt = WordTokenizer(config=config)

    segedLine = []
    tokens = get_tokens(wt, text)
    for token in tokens:
        segedLine.append(token.text.replace(' ', ''))
    
    return segedLine


def get_tokens(wt, text):
    tokens = wt.tokenize(text, split_affixes=False, spaces_as_punct=False)
    return tokens


def text_tokenize(corpus_path, output_path, output_file_name, dialect_name='general', encoding='utf-8'):
    config = Config(dialect_name=dialect_name)
    wt = WordTokenizer(config=config)
    segedText = []
    for line in open(corpus_path, encoding=encoding): 
        segedLine = []
        tokens = get_tokens(wt, line)
        for token in tokens:
            segedLine.append(token.text.replace(' ', ''))
        segedText.append(' '.join(segedLine).strip('\n'))

    with io.open(os.path.join(output_path, output_file_name), 'w', encoding=encoding) as f:
                f.write('\n'.join(segedText))
    
    pass


if __name__ == "__main__":
    # outputPath = 'corpus/'
    # outputFileName = 'segedCorpus.txt'
    # corpusPath = "corpus/corpus.txt"
    # text_tokenize(corpusPath, outputPath, outputFileName, dialect_name='general')
    print(' '.join(sentence_tokenize("བཀྲ་ཤིས་བདེ་ལེགས་ཞུས་རྒྱུ་ཡིན་ སེམས་པ་སྐྱིད་པོ་འདུག།")))