'''
对藏语分词工具botok进行调试
'''
from botok import WordTokenizer
from botok.config import Config
from pathlib import Path
import io
import os

def get_tokens(wt, text):
    tokens = wt.tokenize(text, split_affixes=False, spaces_as_punct=False)
    return tokens

if __name__ == "__main__":
    config = Config(dialect_name="general")
    wt = WordTokenizer(config=config)
    segedText = []
    for line in open("corpus/corpus.txt", encoding='utf-8'): 
        # text = "བཀྲ་ཤིས་བདེ་ལེགས་ཞུས་རྒྱུ་ཡིན་ སེམས་པ་སྐྱིད་པོ་འདུག།"
        segedtLine = []
        tokens = get_tokens(wt, line)
        for token in tokens:
            segedtLine.append(token.text.replace(' ', ''))
        segedText.append(' '.join(segedtLine).strip('\n'))

    output_path = 'corpus/'
    output_file_name = 'segedCorpus.txt'
    with io.open(os.path.join(output_path, output_file_name), 'w', encoding='utf-8') as f:
                f.write('\n'.join(segedText))
                