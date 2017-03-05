class Ispis:

    def __init__(self,output1,output2):
        self.output = output1
        self.output2 = output2

    def shorten(self):
        short = []
        shortout = []
        for i in range(len(self.output)):
            b = str(self.output[i][0][0])
            b = b[2:-5]
            short += [[b]]
            short[-1][0] = short[-1][0].replace('\\r\\','')
            short[-1] = short[-1][0].split('n')


        for i in range(len(self.output2)):
            self.output2[i] = self.output2[i][:-1]

        for i in range(len(self.output2)):
            if self.output2[i-1][0] == '-':
                shortout += [[]]
            if self.output2[i][0] != '-':
                shortout[-1] += [self.output2[i]]

        return short, shortout

def main():
    return
if __name__ == "__main__":
    main()