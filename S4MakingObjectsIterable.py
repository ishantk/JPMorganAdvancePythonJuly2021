class Cube:

    def __init__(self, length):
        self.length = length
        self.number = 1

    def __iter__(self):
        print("[iter] executed. number and length: ", self.number, self.length)
        return self

    def __next__(self):
        print("[next] executed. number and length: ", self.number, self.length)

        if self.number < self.length:
            result = self.number ** 3
            self.number += 1
            return result
        else:
            raise StopIteration


def main():
    cubes = iter(Cube(length=5))
    for c in cubes:
        print(c)

if __name__ == '__main__':
    main()