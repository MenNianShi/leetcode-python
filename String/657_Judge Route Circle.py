# Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.
#
# The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        hor = 0
        ver = 0
        for i in moves:
            if i == 'U':
                ver = ver +1
            if i=='D':
                ver = ver-1
            if i=='L':
                hor = hor+1
            if i=='R':
                hor = hor -1
        if hor ==0 and ver ==0:
            return True
        else:
            return False
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count('L') - moves.count('R') == 0 and moves.count('U') - moves.count('D') == 0