from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, stock):
        simple_report = super().generate(stock)
        products_by_company = cls.get_products_stocked_by_company(stock)
        companies_report = cls.generate_companies_report(products_by_company)

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{companies_report}"
        )

    @staticmethod
    def get_products_stocked_by_company(stock):
        companies = {}
        for product in stock:
            company = product["nome_da_empresa"]
            if company in companies:
                companies[company] += 1
            else:
                companies[company] = 1
        return companies

    @staticmethod
    def generate_companies_report(companies):
        report = "".join(
            f"- {company}: {quantity}\n" for company,
            quantity in companies.items()
        )
        return report
