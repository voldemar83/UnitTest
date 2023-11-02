"""
Скрипт тестирует код main.py
"""

import unittest
from unittest.mock import patch

from main import TwoListsAverageSumCalculator

class TestTwoListsAverageSumCalculator(unittest.TestCase):

    """
    Класс состоит из методов, тестирующих функционал модуля main.py
    """

    def test_correct_lists(self):

        """
        Проверяем корректность записи списков в объект
        """

        lst1 = [2, 5, 9]
        lst2 = [3, 4, 12]
        calculator = TwoListsAverageSumCalculator(lst1, lst2)
        self.assertEqual(calculator.get_lst1(), lst1, "Первый список записывается неверно")
        self.assertEqual(calculator.get_lst2(), lst2, "Второй список записывается неверно")

    def test_lists_average_sum(self):

        """
        Проверяем правильность вычисления среднего значения списка
        """

        lst1 = [2, 5, 9]
        lst2 = [3, 4, 12]
        calculator = TwoListsAverageSumCalculator(lst1, lst2)
        self.assertEqual(calculator.get_lst1_average_sum(), (2 + 5 + 9) / 3,
                         "Среднее значение высчитывается неверно")
        self.assertEqual(calculator.get_lst2_average_sum(), (3 + 4 + 12) / 3,
                         "Среднее значение высчитывается неверно")

        # Проверяем с нулями и отрицательными числами
        lst1 = [0, 0, 0]
        lst2 = [-2, -5, -9]
        calculator = TwoListsAverageSumCalculator(lst1, lst2)
        self.assertEqual(calculator.get_lst1_average_sum(), 0,
                         "Среднее значение высчитывается неверно")
        self.assertEqual(calculator.get_lst2_average_sum(), (-2 - 5 - 9) / 3,
                         "Среднее значение высчитывается неверно")

    def test_empty_list_exception(self):

        """
        Проверяем исключение при передаче пустых списков
        """

        # Оба списка пустые
        lst1 = []
        lst2 = []
        with self.assertRaises(ValueError) as context:
            TwoListsAverageSumCalculator(lst1, lst2)
        self.assertEqual(str(context.exception),
                         "Вы передали пустой список")

        # Первый список пустой
        lst1 = []
        lst2 = [2, 5, 9]
        with self.assertRaises(ValueError) as context:
            TwoListsAverageSumCalculator(lst1, lst2)
        self.assertEqual(str(context.exception),
                         "Вы передали пустой список")

        # Второй список пустой
        lst1 = [2, 5, 9]
        lst2 = []
        with self.assertRaises(ValueError) as context:
            TwoListsAverageSumCalculator(lst1, lst2)
        self.assertEqual(str(context.exception),
                         "Вы передали пустой список")

    # Проверяем вывод сравнения среднего значения списков

    def test_comparison_result_lst1_more_than_lst2(self):

        """
        Проверяем, что среднее значение первого списка больше второго
        """

        lst1 = [3, 4, 12]
        lst2 = [2, 5, 9]
        calculator = TwoListsAverageSumCalculator(lst1, lst2)

        val1 = str((3 + 4 + 12) / 3)
        val2 = str((2 + 5 + 9) / 3)

        # Используем unittest.mock.patch для временного перехвата print
        with patch('builtins.print', side_effect=print) as mock_print:
            calculator.print_comparison_result()
            captured_output = "".join(call.args[0] for call in mock_print.call_args_list)

        # Сравниваем вывод с ожидаемым значением
        self.assertEqual(captured_output,
                         "Первый список имеет большее среднее значение ("+val1+" > "+val2+")")

    def test_comparison_result_lst2_more_than_lst1(self):

        """
        Проверяем, что среднее значение второго списка больше первого
        """

        lst1 = [2, 5, 9]
        lst2 = [3, 4, 12]
        calculator = TwoListsAverageSumCalculator(lst1, lst2)

        val1 = str((2 + 5 + 9) / 3)
        val2 = str((3 + 4 + 12) / 3)

        # Используем unittest.mock.patch для временного перехвата print
        with patch('builtins.print', side_effect=print) as mock_print:
            calculator.print_comparison_result()
            captured_output = "".join(call.args[0] for call in mock_print.call_args_list)

        # Сравниваем вывод с ожидаемым значением
        self.assertEqual(captured_output,
                         "Второй список имеет большее среднее значение ("+val1+" < "+val2+")")

    def test_comparison_result_lst2_equal_lst1(self):

        """
        Проверяем, что среднее значение обоих списков одинаковое
        """

        lst1 = [2, 5, 8]
        lst2 = [3, 7, 5]
        calculator = TwoListsAverageSumCalculator(lst1, lst2)

        val1 = str((2 + 5 + 8) / 3)
        val2 = str((3 + 7 + 5) / 3)

        # Используем unittest.mock.patch для временного перехвата print
        with patch('builtins.print', side_effect=print) as mock_print:
            calculator.print_comparison_result()
            captured_output = "".join(call.args[0] for call in mock_print.call_args_list)

        # Сравниваем вывод с ожидаемым значением
        self.assertEqual(captured_output,
                         "Средние значения списков равны ("+val1+" = "+val2+")")
