class Cube:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.e = 0
        self.w = 0
        self.n = 0
        self.s = 0
        self.t = 0
        self.b = 0
    
    def roll_e(self):
        temp = self.b
        self.b = self.e
        self.e = self.t
        self.t = self.w
        self.w = temp
        self.c += 1
            
    def roll_w(self):
        temp = self.b
        self.b = self.w
        self.w = self.t
        self.t = self.e
        self.e = temp
        self.c -= 1

    def roll_s(self):
        temp = self.b
        self.b = self.s
        self.s = self.t
        self.t = self.n
        self.n = temp
        self.r += 1
    
    def roll_n(self):
        temp = self.b
        self.b = self.n
        self.n = self.t
        self.t = self.s
        self.s = temp
        self.r -= 1
    
    
n, m, cube_r, cube_c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ds = [[None, None], [0, 1], [0, -1], [-1, 0], [1, 0]]
roll_list = list(map(int, input().split()))
cube = Cube(cube_r, cube_c)
cube_roll = [None, cube.roll_e, cube.roll_w, cube.roll_n, cube.roll_s]
for roll in roll_list:
    dr, dc = ds[roll]
    nr, nc = cube.r + dr, cube.c + dc
    if 0 <= nr < n and 0 <= nc < m:
        cube_roll[roll]()
        if arr[nr][nc] == 0:
            arr[nr][nc] = cube.b
        else:
            cube.b = arr[nr][nc]
            arr[nr][nc] = 0
        print(cube.t)