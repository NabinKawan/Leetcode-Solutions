class Solution(object):
    def countStudents(self, students, sandwiches):
        while True:
            if len(students) == 0 or sandwiches[0] not in students:
                break
            elif sandwiches[0] == students[0] : 
                sandwiches.pop(0)
                students.pop(0)
            else:
                item = students.pop(0)
                students.append(item)
        return len(students)
