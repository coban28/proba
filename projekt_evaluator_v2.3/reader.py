class Reader:
    def __init__(self,  input_file = "input.txt", output_file = "output.txt"):
        self.i = input_file
        self.o = output_file
        return
    def read_in(self):
        try:
            file = open(str(self.i), "r")
            L = []
            L = file.readlines()
            return L
        except FileNotFoundError:
            print("Input dokument nije pronađen")
            return
    def read_out(self):
        try:
            file = open(str(self.o),"r")
            L = []
            L = file.readlines()
            return L
        except FileNotFoundError:
            print("Output dokument nije pronađen")
            return

def main():
    return
if __name__ == "__main__":
    main()
