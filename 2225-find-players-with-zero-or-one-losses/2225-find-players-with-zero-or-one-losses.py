class Solution(object):
    def findWinners(self, matches):
        wins = {}
        losses = {}
        
        for i in matches:
            if i[0] not in wins:
                wins[i[0]] = 1
            if i[1] in losses:
                losses[i[1]] -= 1
            else:
                losses[i[1]] = 0

        win = []
        one_loss = []

        for i in wins.keys():
            if i not in losses :
                win.append(i)
        for i in losses.keys():
            if losses[i]==0:
                one_loss.append(i)
        win.sort()
        one_loss.sort()
        return [win, one_loss]
                        