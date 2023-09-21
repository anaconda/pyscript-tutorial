from pyscript import document
from data import sync_load as load
from format import to_html_table

DATA_URL = "https://raw.githubusercontent.com/leriomaggio/pyscript-fetch-resources/main/sample_workbook.xls"


def main():
    book, sheet = load(DATA_URL, sheet_name="Data")
    html_table = to_html_table(sheet)
    target_div = document.querySelector("#excel_table")
    target_div.innerHTML = html_table


main()
