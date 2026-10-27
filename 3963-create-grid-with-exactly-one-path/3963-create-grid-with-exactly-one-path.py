class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['#'] * n for _ in range(m)]
        i,j=0,0
        grid[i][j]="."
        while i<m-1 or j<n-1:
            if j<n-1:
                j+=1
            elif i<m-1:
                i+=1
            grid[i][j]="."
            if i<m-1:
                i+=1
                grid[i][j]="."
        return ["".join(row) for row in grid]