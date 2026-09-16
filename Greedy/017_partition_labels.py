# 763. Partition Labels
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        
        hashmap = Counter(s)
        st = set()
        n = len(s)
        i = 0
        j = 0
        res = []
        while j<n:
            st.add(s[j])
            hashmap[s[j]]-=1
            if hashmap[s[j]] == 0:
                st.remove(s[j])
            if len(st) == 0:
                res.append(j-i+1)
                i=j+1
            j=j+1
        return res



# optimized TC: O(n) SC:O(1) no set used instead track last occurence.
class Solution:
    def partitionLabels(self, s):
        """
        Partition the string into as many parts as possible so that each character appears in at most one part.
        Return the sizes of these partitions.
        """
        # Step 1: Record the last occurrence of each character
        last_occurrence = {char: index for index, char in enumerate(s)}
        
        partitions = []
        start, end = 0, 0  # Initialize the start and end of the current partition

        # Step 2: Iterate through the string to determine partitions
        for current_index, char in enumerate(s):
            # Update the end of the current partition to the farthest last occurrence of any character in the partition
            end = max(end, last_occurrence[char])
            
            # If the current index reaches the end of the partition, record the partition's length
            if current_index == end:
                partition_length = end - start + 1
                partitions.append(partition_length)
                start = current_index + 1  # Move the start to the next index for a new partition

        return partitions
