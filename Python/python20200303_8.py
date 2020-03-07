# M: 立候補者
# N: 有権者
# K: 演説が行われる回数
#
# M人が  0 ~ n 回演説をする
# a_i: i 番目で演説された候補者を示す a_i 番目の候補者

L = []
L = list(map(int, input().rstrip().split()))

M = L[0]
N = L[1]
K = L[2]

for i in range(K):
    M_i = input()

for i in M_i:
    print(M_i)
