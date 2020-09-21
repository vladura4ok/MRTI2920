class MyIter:

    col = [0,1,2,3,4]

    def __iter__(self):
        self.current = -1
        return self

    def __next__(self):
        if self.current == len(self.col) - 1:
            raise StopIteration

        self.current += 1
        return self.col[self.current]

it = MyIter()
for i in it:
    print(i)