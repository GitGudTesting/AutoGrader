import os
import test_eval



class Question1(test_eval.Question):

    def __init__(self):
        self.name = 'fix_is_store_open'
        self.total_points = 10
        self.case_points = self.total_points / len(self.get_tests())
        self.exempted = [4]

    def solution(self, current_time, opening_times):
        current_time = current_time.replace(':', '')
        opening_time_list = opening_times.replace(':', '').split('-')
        start = opening_time_list[0]
        end = opening_time_list[1]
        # you can also explictly convert to int, strings work though:
        if current_time > '2359' or start > '2359' or end > '2359':
            return 'invalid time'
        else:
            return start <= current_time <= end

    def get_tests(self):
        return [
            ("00:00", "01:00-23:59"),
            ("07:00", "00:00-23:59"),
            ("06:34", "06:01-06:59"),
            ("01:00", "01:00-01:00"),
            ("25:00", "23:00-26:00")
        ]


class Question2(test_eval.Question):

    def __init__(self):
        self.name = 'fix_my_function'
        self.total_points = 10
        self.case_points = self.total_points / len(self.get_tests())
        self.exempted = []

    def write_files(self):
        lines = [
            'price: 0',
            'product: shoe',
            'product: shoe, price: 5',
            'product: umbrella, price: 5',
            'price: 2, product: stroopwafels'
        ]
        for i, line in enumerate(lines):
            with open(os.path.dirname(os.path.abspath(__file__)) +
                      f'/test_files/single_order/order{i + 1}.txt', 'w') as fo:
                fo.write(line)

    def solution(self, filename):
        with open(filename, 'r') as f:
            x = f.read()
        if 'price' in x:
            if 'umbrella' in x:
                return 'umbrella'
            elif 'shoe' in x:
                return 'shoe'
            else:
                return False
        elif 'price' not in x and ('umbrella' in x or 'shoe' in x):
            return 'no price'
        else:
            return False

    def get_tests(self):
        return [
            (os.path.dirname(os.path.abspath(__file__)) + '/test_files/single_order/order1.txt'),
            (os.path.dirname(os.path.abspath(__file__)) + '/test_files/single_order/order2.txt'),
            (os.path.dirname(os.path.abspath(__file__)) + '/test_files/single_order/order3.txt'),
            (os.path.dirname(os.path.abspath(__file__)) + '/test_files/single_order/order4.txt'),
            (os.path.dirname(os.path.abspath(__file__)) + '/test_files/single_order/order5.txt')
        ]
