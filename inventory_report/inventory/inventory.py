import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.complete_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        inventory = cls.read(path)
        if type == "simples":
            return SimpleReport.generate(inventory)
        else:
            return CompleteReport.generate(inventory)

    @staticmethod
    def read(path):
        with open(path, mode='r') as file:
            dictionaries = csv.DictReader(file)
            data = []
            for dictionary in dictionaries:
                data.append(dictionary)
            return data
