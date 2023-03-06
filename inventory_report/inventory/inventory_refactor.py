# import csv
# import json
# import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.complete_report import SimpleReport
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def data(self):
        return self.data

    def import_data(self, path, type):
        self.data = [*self.data, *self.importer.import_data(path)]
        if type == "simples":
            return SimpleReport.generate(self.data)
        else:
            return CompleteReport.generate(self.data)
        raise ValueError("Insira um tipo válido")

    def __iter__(self):
        return InventoryIterator(self.data)
