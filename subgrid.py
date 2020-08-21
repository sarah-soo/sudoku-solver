
class Subgrid():
    
    def __init__(self):
        self.content = []


    def populate(self, r1, r2, r3, location):
        i = 0

        while (i < 9):
            if (i <=2):
                if location == "tl":
                    self.content.append(r1[i])
                elif location == "tm":
                    self.content.append(r1[i + 3])
                elif location == "tr":
                    self.content.append(r1[i + 6])
            elif (i > 2) and (i <=5):
                if location == "tl":
                    self.content.append(r2[i - 3])
                elif location == "tm":
                    self.content.append(r2[i])
                elif location == "tr":
                    self.content.append(r2[i + 3])
            elif (i > 5) and (i <= 8):
                if location == "tl":
                    self.content.append(r3[i - 6])
                elif location == "tm":
                    self.content.append(r3[i - 3])
                elif location == "tr":
                    self.content.append(r3[i])
            i += 1

        return self.content

    def check_if_complete(self):
        self.complete = True
        i = 0
        while (i < 9):
            if self.content[i] == 0:
                self.complete = False
            i += 1

        return self.complete