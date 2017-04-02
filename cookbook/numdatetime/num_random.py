# 你想从一个序列中随机抽取若干元素，或者想生成几个随机数
import random


def simple():
    values = [1, 2, 3, 4, 5, 6]
    print(random.choice(values), random.choice(values))
    print(random.sample(values, 2))
    random.shuffle(values)
    print(values)
    # 生成随机整数，请使用random.randint()
    print(random.randint(0, 10), random.randint(0, 10))
    # 为了生成 0 到 1 范围内均匀分布的浮点数，使用 random.random()
    print(random.random())
    # 如果要获取N位随机位(二进制)的整数，使用random.getrandbits()
    print(random.getrandbits(200))


def seed_demo():
    # random模块使用MersenneTwister算法来计算生成随机数。这是一个确定性算法，但是你可以通过
    # random.seed()函数修改初始化种子
    random.seed()  # Seed based on system time or os.urandom()
    random.seed(12345)  # Seed based on integer given
    random.seed(b'bytedata')  # Seed based on byte data
    # 除了上述介绍的功能， random 模块还包含基于均匀分布、高斯分布和其他分布的
    # 随机数生成函数。比如， random.uniform() 计算均匀分布随机数， random.gauss()
    # 计算正态分布随机数。对于其他的分布情况请参考在线文档


# simple()
seed_demo()
