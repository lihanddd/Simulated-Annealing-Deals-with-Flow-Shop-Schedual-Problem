import numpy as np
import math
import random
import time

T0 = 10
min_T = 1e-3
theta = 0.9999
round = 10


def test_arrange(array, arrange, m, n):
    print("+++++++++++++++++++")
    t = evaluate(array, arrange, m, n)
    print("time =", t)
    print("+++++++++++++++++++")


def evaluate(array, arrange, m, n):
    dp = [[0]*n for i in range(m)]
    sum = 0
    for i in range(n):
        sum += array[arrange[i]][0]
        dp[0][i] = sum
    for i in range(1, m):
        for j in range(n):
            if j == 0:
                dp[i][j] = dp[i-1][j] + array[arrange[j]][i]
                continue
            if dp[i-1][j] < dp[i][j-1]:
                dp[i][j] = dp[i][j-1] + array[arrange[j]][i]
                continue
            dp[i][j] = dp[i-1][j] + array[arrange[j]][i]
    return dp[m-1][n-1]


def generat(arrange, n):
    new_arrange = arrange*1  # 乘1使得new_arrange不是引用，而是复制arrange
    a = random.randrange(0, n)
    b = random.randrange(0, n)
    enum = new_arrange[a]
    new_arrange[a] = new_arrange[b]
    new_arrange[b] = enum
    return new_arrange


def simulate(array, m, n):
    t = 0x3f3f3f3f
    T = T0*m*n
    ori_arrange = random.sample(range(0, n), n)  # 随机产生初始解
    while T > 1e-3:
        T = T * theta  # 当前温度
        new_arrange = generat(ori_arrange, n)  # 产生新解
        new_t = evaluate(array, new_arrange, m, n)  # 评估新解
        if new_t < t:  # 接受新解
            t = new_t
            ori_arrange = new_arrange
            continue
        p = math.exp((t - new_t) / T)
        if random.random() <= p:  # 以概率接受新解
            t = new_t
            ori_arrange = new_arrange
            continue
    return t, ori_arrange


if __name__ == '__main__':
    with open("input.txt") as file:
        line = file.readline()
        instance = 0
        while line:
            if line.startswith("instance"):
                num = line.split()[1]
                # if num == '10':
                print("instance"+num+':')
                line = file.readline()
                n, m = line.split()
                data = [list(map(int, file.readline().rstrip().split()))
                        for j in range(int(n))]
                data = np.array(data)[:, 1::2]
                # if instance == 8:
                #     test_arrange(data, [13, 5, 0, 3, 7, 2, 6, 10, 15, 12, 9,
                #                  4, 1, 18, 16, 11, 8, 14, 17, 19], int(m), int(n))  # 测试
                best_time = 0x3f3f3f3f
                best_ans = []
                for i in range(round):
                    start = time.perf_counter()
                    tmp_time, tmp_ans = simulate(data, int(m), int(n))
                    end = time.perf_counter()
                    print("round:", i, "use_time:", end-start)
                    print("tmp_time:",tmp_time)
                    if tmp_time < best_time:
                        best_time = tmp_time
                        best_ans = tmp_ans
                print("bestTime in instance", instance, ":", best_time)
                print("arrange:", best_ans)
                instance += 1
            line = file.readline()
