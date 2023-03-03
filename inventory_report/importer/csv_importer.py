from .importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        inventory = ""
        if path == "inventory_report/data/inventory.csv":
            inventory = cls.read_csv(path)
        else:
            raise ValueError("Arquivo inválido")
        return inventory

    @staticmethod
    def read_csv(path):
        with open(path, mode='r') as file:
            dictionaries = csv.DictReader(file)
            data = []
            for dictionary in dictionaries:
                data.append(dictionary)
            return data
