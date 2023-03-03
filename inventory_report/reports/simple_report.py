from datetime import datetime
from statistics import mode


class SimpleReport:
    @classmethod
    def generate(cls, stock):
        oldest_fabrication = cls.get_oldest_fabrication(stock)
        nearest_expiration_date = cls.get_nearest_expiration_date(stock)
        company_with_most_products = cls.get_company_with_most_products(stock)

        return (
            f"Data de fabricação mais antiga: {oldest_fabrication}\n"
            f"Data de validade mais próxima: {nearest_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_most_products}"
        )

    @staticmethod
    def get_oldest_fabrication(stock):
        return min([product["data_de_fabricacao"] for product in stock])

    @staticmethod
    def get_nearest_expiration_date(stock):
        now = datetime.now().isoformat()
        expiration_dates = [product["data_de_validade"] for product in stock]
        not_expired_dates = [date for date in expiration_dates if date > now]
        return min(not_expired_dates)

    @staticmethod
    def get_company_with_most_products(stock):
        companies = [product["nome_da_empresa"] for product in stock]
        # https://docs.python.org/3/library/statistics.html#statistics.mode
        return mode(companies)
