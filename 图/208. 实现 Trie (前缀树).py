# 对于添加单词，将单词添加到字典树中即可。
#
# 对于搜索单词，从字典树的根结点开始搜索。由于待搜索的单词可能包含点号，因此在搜索过程中需要考虑点号的处理。对于当前字符是字母和点号的情况，分别按照如下方式处理：
#
# 如果当前字符是字母，则判断当前字符对应的子结点是否存在，如果子结点存在则移动到子结点，继续搜索下一个字符，如果子结点不存在则说明单词不存在，返回 false\text{false}false；
#
# 如果当前字符是点号，由于点号可以表示任何字母，因此需要对当前结点的所有非空子结点继续搜索下一个字符。
#
class Trie(object):

    def __init__(self):
        self.children = [ None] * 26

        self.isEnd = False

    def searchPrefix(self,prefix):
        node = self
        for ch in prefix:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.searchPrefix(word)
        return node is not None and node.isEnd


    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.searchPrefix(prefix)
        return node is not None

# 211. 添加与搜索单词 - 数据结构设计.py
