class Solution(object):
    def countStudents(self, students, sandwiches):
        for x in sandwiches:
            if x in students:
                students.remove(x)
            else:
                return len(students)
        return 0