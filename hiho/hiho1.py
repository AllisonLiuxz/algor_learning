"""
def main():
    in_str = raw_input()
    num_str = raw_input()
    in_l = in_str.split()
    in_l = [int(i) for i in in_l]
    num_l = num_str.split()
    num_l = [int(num) for num in num_l]
    n, p, q, k = in_l[0], in_l[1], in_l[2], in_l[3]
    num_l.sort()
    if k == 0:
        print sum(num_l[q:]) - sum(num_l[:q])
    else:
        if q == 0:
            print sum(num_l)
        else:
            print sum(num_l[1:]) - num_l[0]
"""


def main():
    in_str = raw_input()
    in_l = in_str.split()
    in_l = [int(i) for i in in_l]
    i = 0
    qj_l = []
    while i < in_l[0]:
        tmp_str = raw_input()
        tmp_l = tmp_str.split()
        tmp_l = [int(q) for q in tmp_l]
        qj_l.append(tmp_l[0], tmp_l[1])
        i += 1
    qr_l = []
    i = 0
    while i < in_l[1]:
        tmp = input()
        qr_l.append(tmp)
        i += 1

    order_l = []
    qj_l.sort(lambda x, y: x[0]-y[0])



main()
