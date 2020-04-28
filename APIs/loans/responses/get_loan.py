from base.common.models.data_table_response import DataColEntryKeys, RowValueKeys, RowColKeys, DataTableKeys, DataTable
from base.common.response import CommonResponse


class GetLoanResponse(CommonResponse):

    def __init__(self, **kwargs):
        key = DataTableKeys.DATA_TABLE
        model = DataTable

        self._OBJS = [key]
        self._combine_args(objs=self._OBJS)

        kwargs[key] = model(**kwargs.get(key, {}))
        super().__init__(keys=None, objs=self._OBJS, **kwargs)

    def show_data_table(self):
        # FIXME
        table_data = getattr(self, DataTableKeys.DATA_TABLE)
        table = [[getattr(col, DataColEntryKeys.LABEL) for col in
                  getattr(table_data, DataTableKeys.COLS)]]

        for row_dict in getattr(table_data, DataTableKeys.ROWS):
            row_data = [getattr(row, RowValueKeys.VALUE) for row in getattr(row_dict, RowColKeys.COL)]
            table.append(row_data)

        # TODO: Create proper ASCII table via PrettyTable or implement simple array table
        print(table)

class GetLoanDetailResponse(GetLoanResponse):
    pass