import xmltodict
from .importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        inventory = ""
        if path == "inventory_report/data/inventory.xml":
            inventory = cls.read_xml(path)
        else:
            raise ValueError("Arquivo inválido")
        return inventory

    @staticmethod
    def read_xml(path):
        with open(path, mode="r") as file:
            dictionaries = xmltodict.parse(file.read())["dataset"]["record"]
            return dictionaries
