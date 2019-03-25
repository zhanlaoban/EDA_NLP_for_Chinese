# NLP中数据增强的实现

本工具是论文《Easy data augmentation techniques for boosting performance on text classification tasks》的代码实现。原作者虽给出了针对英文语料数据增强的代码实现，但不适合中文语料。我经过对原论文附上的代码的修改，现在推出这个适合中文语料的数据增强EDA的实现。



# 使用方法

1. 先将需要处理的语料按照下面的例子处理好成固定的格式：

0	今天天气不错哦。

1	今天天气不行啊！不能出去玩了。

0	又是阳光明媚的一天！



即，标签+一个制表符\t+内容



2. 命令使用例子：

​	$python code/augment.py --input=train.txt --output=train_augmented.txt --num_aug=16 --alpha=0.05

这里：

input参数：需要进行增强的语料文件

output参数：输出文件

num_aug参数：每一条语料将增强的个数

alpha参数：每一条语料中改动的词所占的比例



具体使用方法同英文语料情况。请参考[eda_nlp](https://github.com/jasonwei20/eda_nlp)。



# 参考/感谢

- 原仓库：[eda_nlp](https://github.com/jasonwei20/eda_nlp)。感谢原作者的付出。Thanks to the author of the paper.

- [jieba分词](https://github.com/fxsjy/jieba)
- [Synonyms](https://github.com/huyingxi/Synonyms)

