'''
实现四种（五种）数据增强方法，并整合起来作为EDA函数供主函数调用
'''
import Tokenizer
import random
import W2v
import Translate


def synonym_replacement(model, segedText):
    augedText = segedText.copy()
    randIndex = random.randint(0, len(augedText) - 1)
    word = augedText[randIndex]
    while word not in model.wv.key_to_index.keys():
        randIndex = random.randint(0, len(augedText) - 1)
        word = augedText[randIndex]
    
    synonym_word = random.choice(W2v.calculate_most_similar(model, word, topn=5))[0]
    augedText[randIndex] = synonym_word

    return ' '.join(augedText)


def random_insert(model, segedText):
    augedText = segedText.copy()
    word = random.choice(augedText)
    while word not in model.wv.key_to_index.keys():
        word = random.choice(augedText)
    
    synonym_word = random.choice(W2v.calculate_most_similar(model, word, topn=5))[0]
    augedText.insert(random.randint(0, len(augedText)), synonym_word)

    return ' '.join(augedText)


def random_delete(segedText):
    augedText = segedText.copy()
    augedText.pop(random.randint(0, len(augedText) - 1))

    return ' '.join(augedText)


def random_swap(segedText):
    augedText = segedText.copy()
    randIndex1 = random.randint(0, len(augedText) - 1)
    randIndex2 = random.randint(0, len(augedText) - 1)
    while randIndex2 == randIndex1:
        randIndex2 = random.randint(0, len(augedText) - 1)
    
    augedText[randIndex1], augedText[randIndex2] = augedText[randIndex2], augedText[randIndex1]

    return ' '.join(augedText)


def back_translation(text, mid, times=3):
    for _ in range(times):
        lang = random.choice(mid)
        mid.remove(lang)
        midText = Translate.translate(text, lang)
    
    augedText = Translate.translate(midText, 'bo')

    return augedText

    
if __name__ == '__main__':
    text = 'བཀྲ་ཤིས་བདེ་ལེགས་ཞུས་རྒྱུ་ཡིན་ སེམས་པ་སྐྱིད་པོ་འདུག།'
    segedText = Tokenizer.sentence_tokenize(text)
    outputModel = 'models/segedCorpus.model'
    model = W2v.load_word2vec_model(outputModel)
    langList = ['en', 'zh', 'de', 'it', 'he', 'ko', 'ja', 'es', 'ru', 'fr']

    print(' '.join(segedText))
    print()
    augedText = []
    for _ in range(2):
        augedText.append(synonym_replacement(model, segedText))
        augedText.append(random_insert(model, segedText))
        augedText.append(random_delete(segedText))
        augedText.append(random_swap(segedText))
        augedText.append(back_translation(text, langList, times=2))
    
    random.shuffle(augedText)
    print('\n'.join(augedText))