from pyscript import document
from data import async_load as load
from format import to_html_table

import asyncio

DATA_URL = "https://raw.githubusercontent.com/leriomaggio/pyscript-fetch-resources/main/sample_workbook.xls"


async def main():
    book, sheet = await load(DATA_URL, sheet_name="Data")
    html_table = to_html_table(sheet)
    target_div = document.querySelector("#excel_table")
    target_div.innerHTML = html_table


asyncio.create_task(main())
