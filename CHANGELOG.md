# Changelog

## [v0.1.0](https://github.com/Hana61/TibetanEDA/releases/tag/v0.1.0) - 2023-12-08

### Added

* 对藏语分词工具botok测试成功

### Todo

* 对分词后的句子尝试使用Word2vec进行嵌入
* 对语料库进行处理，并连接分词工具，获得词表

## [v0.2.0](https://github.com/Hana61/TibetanEDA/releases/tag/v0.2.0) - 2023-12-09

### Added

* 完成数据预处理的编写，将分散的语料库处理为单个语篇，并进一步合成单个文件

### Todo

* 对语料库文件进行处理，按行读取为sentences
* 对语料库进行处理，并连接分词工具，获得词表
* 对分词后的句子尝试使用Word2vec进行嵌入

## [v0.3.0](https://github.com/Hana61/TibetanEDA/releases/tag/v0.3.0) - 2023-12-09

### Added

* 完成分词过程，将分词结果保存为segedCorpus.txt，词间以空格隔开

### Todo

* ~~对语料库文件进行处理，按行读取为sentences~~
* ~~对语料库进行处理，并连接分词工具，获得词表~~
* 对分词后的句子尝试使用Word2vec进行嵌入

## [v0.4.0](https://github.com/Hana61/TibetanEDA/releases/tag/v0.4.0) - 2023-12-10

### Added

* 完成藏文词嵌入过程，将模型保存为segedCorpus.model（模型），segedCorpus.vector（向量），并成功测试同义词检索功能

### Todo

* ~~对语料库文件进行处理，按行读取为sentences~~
* ~~对语料库进行处理，并连接分词工具，获得词表~~
* ~~对分词后的句子尝试使用Word2vec进行嵌入~~
* 编写EDA程序，包含同义词替换（SR），随机插入（RI），随机删除（RD），随机交换（RS）
* 编写回译程序，尝试调用微信翻译API
* 通过汉语编写小型文本分类任务数据集，并进行测试
* 编写文档

## [v0.4.1](https://github.com/Hana61/TibetanEDA/releases/tag/v0.4.1) - 2023-12-10

### Added

* 将其他代码的接口整合到main.py中

## [v0.4.2](https://github.com/Hana61/TibetanEDA/releases/tag/v0.4.2) - 2023-12-10

### Added

* 实现单句分割
* 修改部分函数名

## [v0.5.0](https://github.com/Hana61/TibetanEDA/releases/tag/v0.5.0) - 2023-12-10

### Added

* 完成EDA同义词替换、随机插入、随机删除、随机交换功能
* 完成微软翻译API调用程序编写

### Todo

* ~~对语料库文件进行处理，按行读取为sentences~~
* ~~对语料库进行处理，并连接分词工具，获得词表~~
* ~~对分词后的句子尝试使用Word2vec进行嵌入~~
* ~~编写EDA程序，包含同义词替换（SR），随机插入（RI），随机删除（RD），随机交换（RS）~~
* 完善EDA程序，添加对自定义增强强度的支持
* 尝试调用~~微信~~微软翻译API编写回译程序
* 通过汉语编写小型文本分类任务数据集，并进行测试
* 编写文档

## [v0.5.1](https://github.com/Hana61/TibetanEDA/releases/tag/v0.5.0) - 2023-12-11

### Added

* 完成微软翻译API调用

### Todo

* ~~对语料库文件进行处理，按行读取为sentences~~
* ~~对语料库进行处理，并连接分词工具，获得词表~~
* ~~对分词后的句子尝试使用Word2vec进行嵌入~~
* ~~编写EDA程序，包含同义词替换（SR），随机插入（RI），随机删除（RD），随机交换（RS）~~
* ~~尝试调用微软翻译API编写回译程序~~
* 完善EDA程序，添加对自定义增强强度的支持
* 通过汉语编写小型文本分类任务数据集，并进行测试
* 编写文档

## [v1.0.0](https://github.com/Hana61/TibetanEDA/releases/tag/v1.0.0) - 2023-12-11

### Added

* 完成EDA功能

### Todo

* ~~对语料库文件进行处理，按行读取为sentences~~
* ~~对语料库进行处理，并连接分词工具，获得词表~~
* ~~对分词后的句子尝试使用Word2vec进行嵌入~~
* ~~编写EDA程序，包含同义词替换（SR），随机插入（RI），随机删除（RD），随机交换（RS）~~
* ~~尝试调用微软翻译API编写回译程序~~
* ~~完善EDA程序，添加对自定义增强强度的支持~~
* 添加EDA对文件的支持，设计参数机制
* 通过翻译EDA英文数据集，构造小型文本分类任务数据集，并进行测试
* 编写文档
