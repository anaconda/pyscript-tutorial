import requests
from typing import Union, Optional, Callable

from xlrd import open_workbook
from xlrd import Book, XLRDError
from xlrd.sheet import Sheet

# Sync Calls
from pyodide_http import patch_requests

# Async Calls
from pyodide.http import pyfetch


def extract(content: bytes, sheet_name: str = None) -> Union[Book, Sheet]:
    """"""
    book = open_workbook(file_contents=content)
    try:
        sheet = book.sheet_by_name(sheet_name)
    except XLRDError:
        return book, None
    return book, sheet


def sync_load(data_url: str, sheet_name: str = None) -> Optional[Union[Book, Sheet]]:
    """"""
    patch_requests()  # patch requests and

    r = requests.get(data_url)
    if r.status_code != 200:  # Not OK
        return None
    return extract(r.content, sheet_name=sheet_name)


async def async_load(data_url: str, sheet_name: str = None):
    """"""
    response = await pyfetch(data_url, method="GET")
    content = await response.bytes()
    return extract(content, sheet_name=sheet_name)
