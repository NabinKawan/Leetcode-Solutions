class Solution(object):
    def sortTheStudents(self, score, k):
        self.students = {}
        for i in range(len(score)):
            self.students[i] = score[i][k]

        sorted_list = list(reversed(sorted(self.students.items() , key = lambda item : item[1])))

        self.new_sorted_students = []
        for item in sorted_list:
            self.new_sorted_students.append(score[item[0]])
        
        return self.new_sorted_students
