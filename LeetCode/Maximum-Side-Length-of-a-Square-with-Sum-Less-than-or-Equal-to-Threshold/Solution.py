class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        rows = len(mat)
        cols = len(mat[0])

        maximum = 0

        for i in range(rows):
            for j in range(cols):
                max_side_possible = min(rows - i, cols - j)

                if maximum >= max_side_possible:
                    continue

                summation = 0
                for x in range(maximum):
                    summation += sum(mat[i + x][j:j + maximum])

                for side in range(maximum + 1, max_side_possible + 1):
                    for x in range(side - 1):
                        summation += mat[i + side - 1][j + x]
                        summation += mat[i + x][j + side - 1]

                    summation += mat[i + side - 1][j + side - 1]

                    if summation <= threshold:
                        maximum = side
                    else:
                        break

        return maximum