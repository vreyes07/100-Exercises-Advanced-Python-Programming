class Matrix:
    def __init__(self, matrixStr):
        self.matrix = [[int(i) for i in row.split()] for row in matrixStr.splitlines()]
