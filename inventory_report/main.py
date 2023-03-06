import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from os import path


def __choose_importer(file_extension):
    if file_extension == ".csv":
        return CsvImporter
    if file_extension == ".json":
        return JsonImporter
    if file_extension == ".xml":
        return XmlImporter


def main():
    arguments = sys.argv
    if len(arguments) != 3:
        sys.stderr.write("Verifique os argumentos\n")
        return sys.stderr
    file = arguments[1]
    type = arguments[2]
    file_extension = path.splitext(file)[1]
    importer = __choose_importer(file_extension)
    inventory = InventoryRefactor(importer)
    data = inventory.import_data(file, type)
    print(data, end="")
