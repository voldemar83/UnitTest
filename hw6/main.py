"""
Модуль рассчитывает среднее значение двух списков,
сравнивает эти средние значения и выводит соответствующее сообщение.
"""

class TwoListsAverageSumCalculator:

    """
    Конструктор класса  принимает два списка чисел:
    :param lst1: Первый список
    :param lst1: Второй список
    """

    lst1 = []
    lst2 = []
    lst1_average_sum = 0
    lst2_average_sum = 0

    def __init__(self, lst1, lst2):

        if len(lst1) == 0 or len(lst2) == 0:
            raise ValueError("Вы передали пустой список")
        self.lst1 = lst1
        self.lst2 = lst2
        self.lst1_average_sum = self.calc(lst1)
        self.lst2_average_sum = self.calc(lst2)

    def calc(self, lst):
        """
        Метод высчитывает среднее знечение списка:
        :param lst: список
        :return: среднее значение списка
        """
        elements_sum = 0
        for i in lst:
            elements_sum += i
        return elements_sum / len(lst)

    def get_lst1(self):
        """
        Геттер для получения первого списка
        """
        return self.lst1

    def get_lst2(self):
        """
        Геттер для получения второго списка
        """
        return self.lst2

    def get_lst1_average_sum(self):
        """
        Геттер для получения среднего значения первого списка
        """
        return self.lst1_average_sum

    def get_lst2_average_sum(self):
        """
        Геттер для получения среднего значения второго списка
        """
        return self.lst2_average_sum

    def print_comparison_result(self):
        """
        Метод сравнивает средние значения списка и выводит отчёт о сравнении
        """
        val1 = str(self.lst1_average_sum)
        val2 = str(self.lst2_average_sum)
        if self.lst1_average_sum > self.lst2_average_sum:
            print("Первый список имеет большее среднее значение ("+val1+" > "+val2+")")
        elif self.lst2_average_sum > self.lst1_average_sum:
            print("Второй список имеет большее среднее значение ("+val1+" < "+val2+")")
        else:
            print("Средние значения списков равны ("+val1+" = "+val2+")")


# if __name__ == "__main__":
#     calculator = TwoListsAverageSumCalculator([2, 5, 9], [3, 4, 12])
#     calculator.print_comparison_result()
