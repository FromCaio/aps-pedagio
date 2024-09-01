import abc
from collections import Counter
from datetime import datetime
from control.analysisStrategy import AnalysisStrategy


class OperatorAnalysisStrategy(AnalysisStrategy):
    def analyze(self, toll_payments):
        operator_counts = Counter()
        for payment in toll_payments:
            if payment.operator and payment.operator.name:
                operator_counts[payment.operator.name] += 1
        operators = list(operator_counts.keys())
        counts = list(operator_counts.values())
        return operators, counts

class PeakTimesAnalysisStrategy(AnalysisStrategy):
    def analyze(self, toll_payments):
        hours = [datetime.strptime(payment.date, "%Y-%m-%d %H:%M:%S").hour for payment in toll_payments]
        hour_counts = Counter(hours)
        return hour_counts

class PaymentMethodAnalysisStrategy(AnalysisStrategy):
    def analyze(self, toll_payments):
        method_counts = Counter()
        for payment in toll_payments:
            if payment.method:
                method_counts[payment.method] += 1
        methods = list(method_counts.keys())
        counts = list(method_counts.values())
        return methods, counts