"""
判断robot是否能移动会远点
"""
class Soluntion():
    def judgeCircle(self,moves):
        return moves.count('L') == moves.count("R") and moves.count("U") == moves.count("D")