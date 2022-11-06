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
        self.name = 'reduce_frequencies'
        self.total_points = 20
        self.case_points = self.total_points / len(self.get_tests())
        self.exempted = []

    def solution(self, worker_output):
        frequencies = {}
        for worker in worker_output:
            for word, count in worker.items():
                if word not in frequencies:
                    frequencies[word] = count
                else:
                    frequencies[word] += count
        if not frequencies:
            return 0
        else:
            return max(frequencies.values())

    def get_tests(self):
        return [
            ([{}]),
            ([{'hello': 4, 'stuff': 1, 'things': 0, 'more': 10}]),
            ([{'stuff': 2, 'more': 1}, {'stuff': 1, 'and': 1}]),
            ([{'no': 0}]),
            ([{'stuff': 1, 'more': 1}])
        ]