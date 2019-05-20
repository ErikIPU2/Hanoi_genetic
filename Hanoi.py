class Hanoi:

    def __init__(self, len):
        if len <= 0:
            raise Exception("Len is less than 1")
        self.__tower_len = len
        self.tower = [[], [], []]
        self.tower_pointers = [[], [], []]
        self.__gerate()

    def set_movements(self, movements):
        if len(movements) <= 0:
            raise Exception("movements len need to be great as 0")
        errCont = 0
        for mov in movements:
            if not self._move(mov['sel'], mov['to']):
                errCont += 1
        print(str(errCont) + " Invalid movements")

    def __gerate(self):
        temp = 1
        for i in range(self.__tower_len):
            self.tower[0].append(temp)
            temp += 2
            self.tower[1].append(0)
            self.tower[2].append(0)
            self.tower_pointers[0] = -1
            self.tower_pointers[1] = self.__tower_len-1
            self.tower_pointers[2] = self.__tower_len-1

    def get_graphic(self, tower):
        if (tower < 0) or (tower > 2):
            raise Exception("Invalid Tower")

        temp = ""
        # For each line
        for i in range(self.tower[tower].__len__()):
            if self.tower[tower][i] == 0:
                for j in range(int((2 * self.__tower_len - 1 - 1) / 2)):
                    temp += " "
                temp += "|\n"
            else:
                for j in range(int((2 * self.__tower_len - 1 - self.tower[tower][i]) / 2)):
                    temp += " "
                for j in range(self.tower[tower][i]):
                    temp += "-"
                temp += "\n"
        return temp

    def _check_move(self, tSel, tTo):
        if tSel == tTo or tSel < 0 or tSel > 2 or tTo < 0 or tTo > 2:
            return False

        if self.tower_pointers[tSel] == self.__tower_len-1:
            return False

        if self.tower_pointers[tTo] == self.__tower_len-1:
            return True

        if self.tower[tSel][self.tower_pointers[tSel]+1] < self.tower[tTo][self.tower_pointers[tTo]+1]:
            return True


    def _move(self, tSel, tTo):
        if not self._check_move(tSel, tTo):
            return False
        temp = self.tower[tSel][self.tower_pointers[tSel]+1]
        self.tower[tSel][self.tower_pointers[tSel]+1] = self.tower[tTo][self.tower_pointers[tTo]]
        self.tower[tTo][self.tower_pointers[tTo]] = temp
        self.tower_pointers[tSel] += 1
        self.tower_pointers[tTo] -= 1
        return True