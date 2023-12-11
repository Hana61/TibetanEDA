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

    return augedText


def random_insert(model, segedText):
    augedText = segedText.copy()
    word = random.choice(augedText)
    while word not in model.wv.key_to_index.keys():
        word = random.choice(augedText)
    
    synonym_word = random.choice(W2v.calculate_most_similar(model, word, topn=5))[0]
    augedText.insert(random.randint(0, len(augedText)), synonym_word)

    return augedText


def random_delete(segedText):
    augedText = segedText.copy()
    augedText.pop(random.randint(0, len(augedText) - 1))

    return augedText


def random_swap(segedText):
    augedText = segedText.copy()
    randIndex1 = random.randint(0, len(augedText) - 1)
    randIndex2 = random.randint(0, len(augedText) - 1)
    while randIndex2 == randIndex1:
        randIndex2 = random.randint(0, len(augedText) - 1)
    
    augedText[randIndex1], augedText[randIndex2] = augedText[randIndex2], augedText[randIndex1]

    return augedText


def back_translation(text, mid, times=3):
    langList = mid.copy()
    for _ in range(times):
        lang = random.choice(langList)
        langList.remove(lang)
        midText = Translate.translate(text, lang)
    
    augedText = Translate.translate(midText, 'bo')

    return augedText


def EDA(text, model, sen_n, SR_p=0.1, RI_p=0.1, RD_p=0.1, RS_p=0.1, BT_n=3):
    segedText = Tokenizer.sentence_tokenize(text)
    langList = ['en', 'zh', 'de', 'it', 'he', 'ko', 'ja', 'es', 'ru', 'fr']

    augedText = []

    for i in range(int(sen_n / 5) + 1):

        midText = segedText.copy()
        for _ in range(max(1, int(len(segedText) * SR_p))):
            midText = synonym_replacement(model, midText)
        augedText.append(' '.join(midText))

        midText = segedText.copy()
        for _ in range(max(1, int(len(segedText) * RI_p))):
            midText = random_insert(model, midText)
        augedText.append(' '.join(midText))  

        midText = segedText.copy()
        for _ in range(max(1, int(len(segedText) * RD_p))):
            midText = random_delete(midText)
        augedText.append(' '.join(midText))

        midText = segedText.copy()
        for _ in range(max(1, int(len(segedText) * RS_p))):
            midText = random_swap(midText)
        augedText.append(' '.join(midText))

        midText = back_translation(text, langList, BT_n)
        augedText.append(midText)

    random.shuffle(augedText)

    return augedText[:sen_n]

    
if __name__ == '__main__':
    text = 'བཀྲ་ཤིས་བདེ་ལེགས་ཞུས་རྒྱུ་ཡིན་ སེམས་པ་སྐྱིད་པོ་འདུག།'
    outputModel = 'models/segedCorpus.model'
    model = W2v.load_word2vec_model(outputModel)

    print(text, '\n')
    print('\n'.join(EDA(text, model, 15, 0.5, 0.5, 0.5, 0.5)))