'''
对分词结果使用Word2vec进行嵌入
'''
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence


def train_word2vec_model(segedCorpusPath, outputVector , outputModel):
    model = Word2Vec(sentences=LineSentence(segedCorpusPath),
                    vector_size=100,
                    sg=1,
                    window=5,
                    min_count=5,)
    model.save(outputModel)
    model.wv.save_word2vec_format(outputVector, binary=False)

    pass


def load_word2vec_model(model_path):
    model = Word2Vec.load(model_path)
    return model


def calculate_most_similar(model, word, topn=10):
    similar_words = model.wv.most_similar(word, topn=topn)
    return similar_words


if __name__ == '__main__':
    segedCorpusPath = 'corpus/segedCorpus.txt'
    outputVector = 'models/segedCorpus.vector'
    outputModel = 'models/segedCorpus.model'
    # train_word2vec_model(segedCorpusPath, outputVector, outputModel)
    model = load_word2vec_model(outputModel)
    calculate_most_similar(model, 'བུད་མེད་')