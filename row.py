class Row:
    def __init__(self):
        self.content = []
        self.complete = False   

    def populate(self, row):
        self.content = row

    def check_if_complete(self):
        self.complete = True
        i = 0

        while (i < 9):
            if self.content[i] == 0:
                self.complete = False
            i += 1

        return self.complete