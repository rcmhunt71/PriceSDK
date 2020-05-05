#!/usr/bin/env python

from APIs.configuration.configuration_list import ConfigurationList, ConfigurationListKeys
from base.common.models.data_table_response import (
    DataColEntryKeys, RowValueKeys, DataTableKeys, RowColKeys)
from APIs.loans.responses.get_loan import GetLoanDetailResponse
from tests.common.common_response_args import response_args
from base.common.response import CommonResponseKeys

# ---------------------------------------------------------------
#     TEST DATA
# ---------------------------------------------------------------

config_list = [
    "Mr.",
    "Mrs.",
    "Ms.",
    "Miss",
    "Dr.",
]

loan_detail_data_column_args_1 = {
    DataColEntryKeys.ID: "Loan_Number_ID",
    DataColEntryKeys.TYPE: "number",
}

loan_detail_data_column_args_2 = {
    DataColEntryKeys.ID: "Status_ID",
    DataColEntryKeys.TYPE: "number",
}

loan_detail_data_column_args_3 = {
    DataColEntryKeys.ID: "Owner_Name",
    DataColEntryKeys.TYPE: "string",
}

loan_detail_data_columns_list = [loan_detail_data_column_args_3, loan_detail_data_column_args_1,
                                 loan_detail_data_column_args_2]

loan_detail_value_entry_1 = {RowValueKeys.VALUE: "Errol Flynn"}
loan_detail_value_entry_2 = {RowValueKeys.VALUE: 5}
loan_detail_value_entry_3 = {RowValueKeys.VALUE: 500}

loan_detail_value_entry_4 = {RowValueKeys.VALUE: "Burt Reynolds"}
loan_detail_value_entry_5 = {RowValueKeys.VALUE: 7}
loan_detail_value_entry_6 = {RowValueKeys.VALUE: 700}

loan_detail_value_entry_7 = {RowValueKeys.VALUE: "Maverick"}
loan_detail_value_entry_8 = {RowValueKeys.VALUE: 10}
loan_detail_value_entry_9 = {RowValueKeys.VALUE: 1000}

loan_detail_col_values_list_1 = [loan_detail_value_entry_1, loan_detail_value_entry_2, loan_detail_value_entry_3]
loan_detail_col_values_list_2 = [loan_detail_value_entry_4, loan_detail_value_entry_5, loan_detail_value_entry_6]
loan_detail_col_values_list_3 = [loan_detail_value_entry_7, loan_detail_value_entry_8, loan_detail_value_entry_9]

loan_detail_col_value_dict_1 = {RowColKeys.COL: loan_detail_col_values_list_1}
loan_detail_col_value_dict_2 = {RowColKeys.COL: loan_detail_col_values_list_2}
loan_detail_col_value_dict_3 = {RowColKeys.COL: loan_detail_col_values_list_3}

loan_detail_row_datum_1 = [loan_detail_col_value_dict_1, loan_detail_col_value_dict_2,
                           loan_detail_col_value_dict_3]

loan_detail_data_table = {DataTableKeys.COLS: loan_detail_data_columns_list,
                          DataTableKeys.ROWS: loan_detail_row_datum_1}


# ---------------------------------------------------------------
#   VALIDATION SECTION
# ---------------------------------------------------------------
config_args = response_args.copy()
config_args[ConfigurationListKeys.CONFIGURATION_LIST] = config_list
configuration = ConfigurationList(**config_args)
print(f"CONFIGURATION LIST:\n{configuration}")

loan_detail_data = response_args.copy()
loan_detail_data[DataTableKeys.DATA_TABLE] = loan_detail_data_table
loan_detail_resp = GetLoanDetailResponse(**loan_detail_data)
loan_detail_resp.show_data_table()
print(f"RAW STATS DATA: {getattr(loan_detail_resp, CommonResponseKeys.STATS).raw}")
print(f"VERSION: {loan_detail_resp.Version.full_version_info()}\n")
