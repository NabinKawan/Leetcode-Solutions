class Solution(object):
    def judgeCircle(self, moves):
        self.initial = [0,0]
        for i in range(len(moves)):
          if moves[i] == 'U':
            self.initial[0] += 1
          elif moves[i] == 'D':
            self.initial[0] -= 1
          elif moves[i] == 'L':
            self.initial[1] == -1
          elif moves[i] == 'R':
            self.initial[1] += 1
        return self.initial[0,0] == [0,0]