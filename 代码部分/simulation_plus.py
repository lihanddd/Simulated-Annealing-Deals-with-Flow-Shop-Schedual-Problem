import numpy as np
import math
import time
import random

T0 = 1000
min_T = 1e-4
theta = 0.9999
round = 10


def test_arrange(array, arrange, m, n):
    print("+++++++++++++++++++")
    t = evaluate(array, arrange, m, n)
    print("time =", t)
    print("+++++++++++++++++++")


def evaluate(array, arrange, m, n):
    dp = np.array([[0]*n for i in range(m)])
    sum = 0
    for i in range(n):  # 处理第一个机器
        sum += array[arrange[0][i]][0]
        dp[0][i] = sum
    for i in range(1, m):  # 处理后边的机器
        for j in range(n):
            k = -1
            for q in range(n):
                if arrange[i-1][q] == arrange[i][j]:
                    k = q
            if dp[i-1][k] < dp[i][j-1]:
                dp[i][j] = dp[i][j-1] + array[arrange[i][j]][i]
                continue
            dp[i][j] = dp[i-1][k] + array[arrange[i][j]][i]
    return dp[m-1][n-1]


def generat(arrange, m, n):
    new_arrange = np.array(arrange, copy=True)
    machine_num = random.randrange(0, m)
    a = random.randrange(0, n)
    b = random.randrange(0, n)
    tmp = new_arrange[machine_num][a]
    new_arrange[machine_num][a] = new_arrange[machine_num][b]
    new_arrange[machine_num][b] = tmp
    return new_arrange


def simulate(array, m, n):
    t = 0x3f3f3f3f
    T = T0*m
    ori_arrange = []
    tmp_arrange = random.sample(range(0, n), n)
    for i in range(m):  # 随机产生初始解
        ori_arrange.append(tmp_arrange)
    ori_arrange = np.array(ori_arrange)
    while T > min_T:
        T = T * theta  # 当前温度
        new_arrange = generat(ori_arrange, m, n)  # 产生新解
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
                # if num == '6':
                print("instance"+num+':')
                line = file.readline()
                n, m = line.split()
                data = [list(map(int, file.readline().rstrip().split()))
                        for j in range(int(n))]
                data = np.array(data)[:, 1::2]
                # if instance == 1:
                # test_arrange(data, [[13, 1, 15, 8, 11, 10, 18, 7, 19, 9, 3, 12, 2, 4, 14, 0, 17, 16, 6, 5],[13, 1, 15, 8, 11, 10, 18, 7, 19, 9, 3, 12, 2, 4, 14, 0, 17, 16, 6, 5],[13, 1, 15, 8, 11, 10, 18, 7, 19, 9, 3, 12, 2, 4, 14, 0, 17, 16, 6, 5],[13, 1, 15, 8, 11, 10, 18, 7, 19, 9, 3, 12, 2, 4, 14, 0, 17, 16, 6, 5],[13, 1, 15, 8, 11, 10, 18, 7, 19, 9, 3, 12, 2, 4, 14, 0, 17, 16, 6, 5],[13, 1, 15, 8, 11, 10, 18, 7, 19, 9, 3, 12, 2, 4, 14, 0, 17, 16, 6, 5],[13, 1, 15, 8, 11, 10, 18, 7, 19, 9, 3, 12, 2, 4, 14, 0, 17, 16, 6, 5],[13, 1, 15, 8, 11, 10, 18, 7, 19, 9, 3, 12, 2, 4, 14, 0, 17, 16, 6, 5],[13, 1, 15, 8, 11, 10, 18, 7, 19, 9, 3, 12, 2, 4, 14, 0, 17, 16, 6, 5],[13, 1, 15, 8, 11, 10, 18, 7, 19, 9, 3, 12, 2, 4, 14, 0, 17, 16, 6, 5],[13, 1, 15, 8, 11, 10, 18, 7, 19, 9, 3, 12, 2, 4, 14, 0, 17, 16, 6, 5],[13, 1, 15, 8, 11, 10, 18, 7, 19, 9, 3, 12, 2, 4, 14, 0, 17, 16, 6, 5],[13, 1, 15, 8, 11, 10, 18, 7, 19, 9, 3, 12, 2, 4, 14, 0, 17, 16, 6, 5],[13, 1, 15, 8, 11, 10, 18, 7, 19, 9, 3, 12, 2, 4, 14, 0, 17, 16, 6, 5],[13, 1, 15, 8, 11, 10, 18, 7, 19, 9, 3, 12, 2, 4, 14, 0, 17, 16, 6, 5],[13, 1, 15, 8, 11, 10, 18, 7, 19, 9, 3, 12, 2, 4, 14, 0, 17, 16, 6, 5],[13, 1, 15, 8, 11, 10, 18, 7, 19, 9, 3, 12, 2, 4, 14, 0, 17, 16, 6, 5],[13, 1, 15, 8, 11, 10, 18, 7, 19, 9, 3, 12, 2, 4, 14, 0, 17, 16, 6, 5],[13, 1, 15, 8, 11, 10, 18, 7, 19, 9, 3, 12, 2, 4, 14, 0, 17, 16, 6, 5],[13, 1, 15, 8, 11, 10, 18, 7, 19, 9, 3, 12, 2, 4, 14, 0, 17, 16, 6, 5]], int(m), int(n))  # 测试
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
                print("arrange:\n", best_ans)
                instance += 1
            line = file.readline()
