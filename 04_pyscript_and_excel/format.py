from xlrd.sheet import Sheet


TABLE_TAG = "<table><thead>{header}</thead><tbody>{body}</tbody></table>"


def to_html_table(sheet: Sheet, template_table_tag: str = TABLE_TAG) -> str:
    """"""
    template_row_tag = "<tr>{cells}</tr>"

    header_row = template_row_tag.format(
        cells=f"{''.join(['<th>{}</th>' for _ in range(sheet.ncols)])}"
    )
    body_row = template_row_tag.format(
        cells=f"{''.join(['<td>{}</td>' for _ in range(sheet.ncols)])}"
    )

    tbody = ""
    for rx in range(sheet.nrows):
        row_text = list(map(lambda entry: entry.value, sheet.row(rx)))
        if rx == 0:  # first row: header
            thead = header_row.format(*row_text)
        else:
            tbody += body_row.format(*row_text)

    return template_table_tag.format(header=thead, body=tbody)
