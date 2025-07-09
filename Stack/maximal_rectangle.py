class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        cols = len(matrix[0])
        heights = [0]*(cols+1)
        max_area=0
        for row in matrix:
            for i in range(cols):
                heights[i] = heights[i]+1 if row[i] == '1' else 0
            stack = []
            for i in range(cols+1):
                while stack and heights[stack[-1]]>heights[i]:
                    h = heights[stack.pop()]
                    w = i if not stack else i-stack[-1]-1
                    if max_area < h*w:
                        max_area = h*w
                stack.append(i)
        return max_area
