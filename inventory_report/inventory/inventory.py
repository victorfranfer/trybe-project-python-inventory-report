import csv
import json
import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.complete_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        inventory = ""
        if path == "inventory_report/data/inventory.csv":
            inventory = cls.read_csv(path)
        elif path == "inventory_report/data/inventory.json":
            inventory = cls.read_json(path)
        else:
            inventory = cls.read_xml(path)
        if type == "simples":
            return SimpleReport.generate(inventory)
        else:
            return CompleteReport.generate(inventory)

    @staticmethod
    def read_csv(path):
        with open(path, mode='r') as file:
            dictionaries = csv.DictReader(file)
            data = []
            for dictionary in dictionaries:
                data.append(dictionary)
            return data

    @staticmethod
    def read_json(path):
        with open(path, mode='r') as file:
            dictionaries = json.load(file)
            return dictionaries

    @staticmethod
    def read_xml(path):
        with open(path, mode="r") as file:
            dictionaries = xmltodict.parse(file.read())["dataset"]["record"]
            return dictionaries
