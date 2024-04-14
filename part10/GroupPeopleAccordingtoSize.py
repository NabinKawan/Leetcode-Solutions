class Solution(object):
    def groupThePeople(self, groupSizes):
        
        bucket = {}

        for i in range(len(groupSizes)):

            if groupSizes[i] in bucket:
                
                inserted = False
                for row in bucket[groupSizes[i]]:
                    if len(row) < groupSizes[i]:
                        row.append(i)
                        inserted = True
                
                if not inserted:
                    bucket[groupSizes[i]].append([i])
                
            else:
                bucket[groupSizes[i]] = [[i]]
        
        result = []
        
        for groups in bucket.values():
            for group in groups:
                result.append(group)
        
        return result
