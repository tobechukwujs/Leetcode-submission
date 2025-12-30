class Solution(object):
    def countStudents(self, students, sandwiches):
        n = len(students)
        q = deque(students)
        res = n

        for sandwich in sandwiches:
            cnt = 0
            while cnt < n and q[0] != sandwich:
                cur = q.popleft()
                q.append(cur)
                cnt +=1 

            if q[0] == sandwich:
                cur = q.popleft()
                res -= 1
            else:
                break    
        return res            
