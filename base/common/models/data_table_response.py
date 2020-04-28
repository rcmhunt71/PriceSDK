import pprint
from dataclasses import dataclass


@dataclass
class DataColEntryKeys:
    ID: str = "id"
    LABEL: str = "label"
    TYPE: str = "type"


@dataclass
class RowValueKeys:
    VALUE: str = "v"


@dataclass
class RowColKeys:
    COL: str = "c"


@dataclass
class DataTableKeys:
    DATA_TABLE: str = "Data"
    COLS: str = "cols"
    ROWS: str = "rows"


class DataTable(list):
    def __init__(self, **kwargs):
        super().__init__()
        self.json = kwargs
        self._table_dict = self._build_table_dict()
        self.extend(self._build_table_rows())

    def as_dict(self):
        return self._table_dict

    def __str__(self):
        return pprint.pformat(self._table_dict)

    def _build_table_dict(self):
        columns = self.json.get(DataTableKeys.COLS, [])
        rows = self.json.get(DataTableKeys.ROWS, [])
        # Each column name is a key in the dictionary
        table = dict([(col.get(DataColEntryKeys.LABEL), []) for col in columns])
        # Iterate through the values lists
        for datum in rows:
            # for each row, append the value to each corresponding column's value list.
            for col_index, col in enumerate(columns):
                value = datum.get(RowColKeys.COL)[col_index].get(RowValueKeys.VALUE)
                table[col.get(DataColEntryKeys.LABEL)].append(value)
        return table

    def _build_table_rows(self):
        table_rows = []

        cols = self.json.get(DataTableKeys.COLS)
        for row in self.json.get(DataTableKeys.ROWS):
            row_object = Row()
            row_data = row.get(RowColKeys.COL)
            if len(row_data) != len(cols):
                raise ValueError('mismatch between number of fields and values')
            for field, value in zip(cols, row_data):
                field_id = field.get(DataColEntryKeys.ID)
                value_content = value.get(RowValueKeys.VALUE)
                if field_id == 'Data':
                    raw_data = Row()
                    for line in value_content.splitlines():
                        if not line.count('='):
                            continue
                        raw_data_field, raw_data_value = line.split('=', 1)
                        setattr(raw_data, raw_data_field, raw_data_value)
                    value_content = raw_data
                setattr(row_object, field_id, value_content)
            table_rows.append(row_object)
        return table_rows


class Row(object):
    def attributes(self):
        return list(self.__dict__.keys())

    def as_dict(self):
        return self.__dict__