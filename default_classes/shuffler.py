from random import randint


class Shuffler:

    def __init__(self, array):
        self.array = array

    def rand_two_part_shuffle(self):
        """
        :return: shuffled list
        """
        # moves item from current index to random list index
        for ind, var in enumerate(self.array):
            index = self.array[ind] - 1
            ran_ind = self.array[randint(0, (len(self.array) - 1))] - 1
            self.array[index], self.array[ran_ind] = self.array[ran_ind], self.array[index]
        return self.array
