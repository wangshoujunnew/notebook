import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords


# 特征提取函数
def extract_features(word_list):
    return dict([(word, True) for word in word_list])


# print(extract_features(['hello','word']))
positive_fileids = movie_reviews.fileids('pos')
negative_fileids = movie_reviews.fileids('neg')
# print(positive_coment)
features_positive = [(extract_features(movie_reviews.words(fileids=[f])), 'Positive') for f in positive_fileids]
features_negative = [(extract_features(movie_reviews.words(fileids=[f])),
                      'Negative') for f in negative_fileids]

# print(features_negative)
# print(features_positive[0])

threshold_factor = 0.8  # 80% 的训练集
threshold_positive = int(threshold_factor * len(features_positive))
threshold_negative = int(threshold_factor * len(features_negative))

# 80% 的积极评论 + 80%的消极评论 = 训练集
features_train = features_positive[:threshold_positive] + \
                 features_negative[:threshold_negative]
features_test = features_positive[threshold_positive:] + \
                features_negative[threshold_negative:]

# print(features_train[0])  # 数据格式
'''
({}, 'Positive') 1: 句子字典 2: 感情
'''
# print("Number of training datapoints: %d" % len(features_train))

# print
# "Number of test datapoints:", len(features_test)

classifier = NaiveBayesClassifier.train(features_train)
# print("Accuracy of the classifier: %s" % nltk.classify.util.accuracy(classifier,
#                                                                      features_test))

for item in classifier.most_informative_features()[:10]: # 最能代表信息的10个词
    print(item)

