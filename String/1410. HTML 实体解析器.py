class Solution(object):
    def entityParser(self, text):
        """
        :type text: str
        :rtype: str
        """
        entityMap = {"&quot;":"\"", "&apos;":"'","&amp;":"&","&gt;":">", "&lt;":"<", "&frasl;":"/",}
        i = 0
        n = len(text)
        res = []
        while i < n:
            isEntity = False
            if text[i] == '&':
                for e in entityMap:
                    if text[i:i+len(e)] == e :
                        res.append(entityMap[e])
                        isEntity = True
                        i+=len(e)
                        break
            if not isEntity:
                res.append(text[i])
                i+=1
        return ''.join(res)