# TibetanEDA

TibetanEDA based on Easy Data Augmentation

## Codes

* dataProcesser.py：用于数据预处理
* draw.ipynb：用于生成报告所需的图像
* eda.py：实现数据增强方法
* main.py：调用各文件接口，实现数据增强功能
* text_classification.ipynb：用于测试的二分类文本分类任务
* Tokenizer.py：藏文分词程序
* Translate：翻译程序（需使用者自行设置微软翻译APIKey）
* W2v.py：藏文词嵌入程序

## corpus

* corpus.txt：用于训练词向量的藏文语料库，未进行分词
* segedCorpus.txt：用于训练词向量的藏文语料库，已分词
* sst2_train_500_zh_bo.txt：增强前的文本分类语料库
* sst2_train_500_zh_bo_5.txt：增强五条后的文本分类语料库
* sst2_train_500_zh_bo_15.txt：增强15条后的文本分类语料库

## references

[EDA: Easy Data Augmentation techniques for boosting performance on text classification tasks.](https://arxiv.org/abs/1901.11196)

[https://github.com/OpenPecha/Botok]([https://github.com/OpenPecha/Botok]())

[https://github.com/Esukhia/botok-data/releases/tag/v0.0.1]([https://github.com/Esukhia/botok-data/releases/tag/v0.0.1]())

[https://github.com/tibetan-nlp/modern-tibetan-corpus](https://github.com/tibetan-nlp/modern-tibetan-corpus)

[https://github.com/tibetan-nlp/classical-tibetan-corpus](https://github.com/tibetan-nlp/classical-tibetan-corpus)

[https://github.com/jasonwei20/eda_nlp](https://github.com/jasonwei20/eda_nlp)

[https://github.com/zhanlaoban/EDA_NLP_for_Chinese](https://github.com/zhanlaoban/EDA_NLP_for_Chinese)
