'''
对藏语分词工具botok进行调试
'''
from botok import WordTokenizer
from botok.config import Config
from pathlib import Path

def get_tokens(wt, text):
    tokens = wt.tokenize(text, split_affixes=False)
    return tokens

if __name__ == "__main__":
    config = Config(dialect_name="kangyur")  # , base_path= Path.home()
    wt = WordTokenizer(config=config)
    text = "བཀྲ་ཤིས་བདེ་ལེགས་ཞུས་རྒྱུ་ཡིན་ སེམས་པ་སྐྱིད་པོ་འདུག།"
    tokens = get_tokens(wt, text)
    print(text)
    for token in tokens:
        print(token.text, end=' ')