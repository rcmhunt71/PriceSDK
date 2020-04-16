from APIs.loans.models.add_loan_data import (
    LoanDataTableKeys, LoanDataColEntryKeys, LoanRowValueKeys, LoanRowColKeys)
from base.common.response import CommonResponse

import pprint


class DataTable:
    def __init__(self, **kwargs):
        self.json = kwargs
        self._table_dict = self._build_table_dict()
        self._table_list = self._build_table_object()

    def as_dict(self):
        return self._table_dict

    def as_list(self):
        return self._table_list

    def __str__(self):
        return pprint.pformat(self._table_dict)

    def _build_table_dict(self):
        columns = self.json.get(LoanDataTableKeys.COLS, [])
        rows = self.json.get(LoanDataTableKeys.ROWS, [])
        # Each column name is a key in the dictionary
        table = dict([(col.get(LoanDataColEntryKeys.LABEL), []) for col in columns])
        # Iterate through the values lists
        for datum in rows:
            # for each row, append the value to each corresponding column's value list.
            for col_index, col in enumerate(columns):
                value = datum.get(LoanRowColKeys.COL)[col_index].get(LoanRowValueKeys.VALUE)
                table[col.get(LoanDataColEntryKeys.LABEL)].append(value)
        return table

    def _build_table_object(self):
        table_object_list = []

        cols = self.json.get(LoanDataTableKeys.COLS)
        for row in self.json.get(LoanDataTableKeys.ROWS):
            table_object = Object()
            row_data = row.get(LoanRowColKeys.COL)
            if len(row_data) != len(cols):
                raise ValueError('mismatch between number of fields and values')
            for field, value in zip(cols, row_data):
                field_id = field.get(LoanDataColEntryKeys.ID)
                value_content = value.get(LoanRowValueKeys.VALUE)
                if field_id == 'Data':
                    raw_data = Object()
                    for line in value_content.splitlines():
                        if not line.count('='):
                            continue
                        raw_data_field, raw_data_value = line.split('=', 1)
                        setattr(raw_data, raw_data_field, raw_data_value)
                    value_content = raw_data
                setattr(table_object, field_id, value_content)
            table_object_list.append(table_object)
        return table_object_list


class Object(object):
    pass


class GetLoanResponse(CommonResponse):

    def __init__(self, **kwargs):
        key = LoanDataTableKeys.DATA_TABLE
        model = DataTable

        self._OBJS = [key]
        self._combine_args(objs=self._OBJS)

        kwargs[key] = model(**kwargs.get(key, {}))
        super().__init__(keys=None, objs=self._OBJS, **kwargs)

    def show_data_table(self):
        # FIXME
        table_data = getattr(self, LoanDataTableKeys.DATA_TABLE)
        table = [[getattr(col, LoanDataColEntryKeys.LABEL) for col in
                  getattr(table_data, LoanDataTableKeys.COLS)]]

        for row_dict in getattr(table_data, LoanDataTableKeys.ROWS):
            row_data = [getattr(row, LoanRowValueKeys.VALUE) for row in getattr(row_dict, LoanRowColKeys.COL)]
            table.append(row_data)

        # TODO: Create proper ASCII table via PrettyTable or implement simple array table
        print(table)
