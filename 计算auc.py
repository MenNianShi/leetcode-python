def naive_auc(labels, preds):
    '''
　　　先排序，然后统计有多少正负样本对满足：正样本预测值>负样本预测值, 再除以总的正负样本对个数
     复杂度 O(NlogN), N为样本数
    '''
    pos_cnt = sum(labels)
    neg_cnt = len(labels)-pos_cnt
    labels_preds = zip(labels,preds)
    labels_preds = sorted(labels_preds,key = lambda x :x[1])
    accumulated_neg = 0
    satisfied_pair = 0
    for i in range(len(labels_preds)):
        if labels_preds[i][0]==1:
            satisfied_pair += accumulated_neg
        else:
            accumulated_neg += 1
    return satisfied_pair / (pos_cnt*neg_cnt)


def approximate_auc(labels, preds, n_bins=100):
    """
    近似方法，将预测值分桶(n_bins)，对正负样本分别构建直方图，再统计满足条件的正负样本对
    复杂度 O(N)
    这种方法有什么缺点？怎么分桶？
    """
    n_pos = sum(labels)
    n_neg = len(labels) - n_pos
    total_pair = n_pos * n_neg

    pos_histogram = [0 for _ in range(n_bins)]
    neg_histogram = [0 for _ in range(n_bins)]
    bin_width = 1.0 / n_bins
    for i in range(len(labels)):
        nth_bin = int(preds[i] / bin_width)
        if labels[i] == 1:
            pos_histogram[nth_bin] += 1
        else:
            neg_histogram[nth_bin] += 1

    accumulated_neg = 0
    satisfied_pair = 0
    for i in range(n_bins):
        satisfied_pair += (pos_histogram[i] * accumulated_neg + pos_histogram[i] * neg_histogram[i] * 0.5)
        accumulated_neg += neg_histogram[i]

    return satisfied_pair / float(total_pair)

import wget

print("downloading with urllib")
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data'
print("downloading with urllib")
wget.download(url,"./")
