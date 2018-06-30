import sys

class polynome:
    
    def __init__(self, s):
        self.s = s
        self.arg = s.split(" ")

    def resolve(self):
        for s in self.s:
            print(s)

def main():
    print(sys.argv)
    if (sys.argv[1] is False):
        return 
    test = polynome(sys.argv[1])
    test.resolve()

if __name__ == "__main__":
    main()
