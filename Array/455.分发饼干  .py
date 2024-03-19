def findContentChildren(g, s):
    """
    :type g: List[int]
    :type s: List[int]
    :rtype: int
    """
    #很容易想到，每个孩子尽量拿到和他想要的大小差距最小的饼干，
    # 就能保证不会“浪费”大块饼干。因此把g和s排序后，把最相邻的饼干分给刚刚好满足的孩子
    # ，就能得到最大的满足数量了。
    g=sorted(g)
    s=sorted(s)

    count = 0
    i,j=0,0
    while j<len(s) and i<len(g):
        if g[i]<=s[j]:
            count+=1
            i+=1
        j+=1
    return count

def findContentChildren( g, s):
    """
    :type g: List[int]
    :type s: List[int]
    :rtype: int
    """

    g = sorted(g, reverse=True);
    s = sorted(s, reverse=True);
    sSize = len(s);

    if sSize == 0:
        return 0;

    k = 0;
    content = 0;

    for x in g:
        if x <= s[k]:
            content += 1;

            k += 1;
            if k >= sSize:
                break;

    return content;
print(findContentChildren([2,4,3],[1,2,3]))

# 455.分发饼干  .py