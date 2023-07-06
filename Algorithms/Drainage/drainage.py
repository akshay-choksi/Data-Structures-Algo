'''
Akshay Choksi (ajc9yr)
Module 5: Drainage (solved with DP + DFS)
11/9/2022
''' 
class drainage:

    #recursive DFS
    def search(self, stored, matrix, rows, columns, i, j, val):
        if i < 0 or j < 0 or rows <= i  or j >= columns or val >= matrix[i][j]:
            return 0
        
        if stored[i][j] != 101:
            return stored[i][j]
        else:
            # do the dfs
            val = matrix[i][j]
            #right val
            r = self.search(stored, matrix, rows, columns, i, j + 1, val)
            #left val
            l = self.search(stored, matrix, rows, columns, i, j - 1, val)
            #upper val
            u = self.search(stored, matrix, rows, columns,i - 1, j, val)
            #down val
            d = self.search(stored, matrix, rows, columns,i + 1, j, val)
            
            stored[i][j] =  1 + max(r, l, u, d)
            return stored[i][j]

    #driving function
    def drain_path(self, rows, columns, matrix):
            stored = [[101 for i in range(columns)] for _ in range(rows)]
            ret = 1
            for x in range(rows):
                for y in range(columns):
                    ret = max(self.search(stored, matrix, rows, columns, x, y, -101), ret)
            return ret
    
            
    #read in input
d = drainage()
city_to_length = {}
cases = int(input())
for _ in range(cases):
    drain_vals = []
    city, rows, columns = input().split()
    rows, columns = int(rows), int(columns)
    for x in range(rows):
        raw = input()
        vals =  list(map(int, raw.split()))
        drain_vals.append(vals)
    length = d.drain_path(rows, columns, drain_vals)
    city_to_length[city] = length

#print from dict
for key, value in city_to_length.items():
    print(key + ": " + str(value))



    '''
    4
    Charlottesville 5 5
    66 78 41 3 77
    4 90 41 8 68
    12 11 29 24 53
    0 51 58 9 28
    97 99 96 58 92
    Richmond 3 3
    1 1 1
    1 1 1
    1 1 1
    WashingtonDC 5 5
    10 81 28 2 49
    64 59 61 85 82
    77 14 81 6 76
    37 86 99 11 92
    85 95 78 13 57
    Wintergreen 5 5
    1 2 3 4 5
    10 9 8 7 6
    11 12 13 14 15
    20 19 18 17 16
    21 22 23 24 25

    '''