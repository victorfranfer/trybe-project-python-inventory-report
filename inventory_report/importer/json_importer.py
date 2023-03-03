import json
from .importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        inventory = ""
        if path == "inventory_report/data/inventory.json":
            inventory = cls.read_json(path)
        else:
            raise ValueError("Arquivo inválido")
        return inventory

    @staticmethod
    def read_json(path):
        with open(path, mode='r') as file:
            dictionaries = json.load(file)
            return dictionaries
