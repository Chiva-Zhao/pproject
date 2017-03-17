# 怎样找出一个序列中出现次数最多的元素呢？

from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']


def default():
    word_count = Counter(words)
    print(word_count, word_count.most_common(2))
    print(word_count['the'])

    for word in morewords:
        word_count[word] += 1
    print(word_count['eyes'])

    word_count.update(morewords)
    print(word_count)


def compute():
    a = Counter(words)
    b = Counter(morewords)
    print(a)
    print(b)
    print(a + b)
    print(a - b)


compute()
