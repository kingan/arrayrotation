
class arrayRot():
    def __init__(self, array, rotation):
        self.array = array
        self.rotation = rotation

    def rotate(self):
        if(self.array):
            for i in range(self.rotation):
                tmp = self.array.pop()
                self.array = [tmp] + self.array
        return self.array


if __name__ == "__main__":
     #arr = [3,8,9,7,6]
     arr = []
     a = arrayRot(arr, 3)
     print a.rotate()
