from dataclasses import dataclass

from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class GetVirtualDataGridRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    TABLE_NAME: str = "Tablename"


class GetVirtualDataGridRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, table_name, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.table_name = table_name
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[GetVirtualDataGridRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[GetVirtualDataGridRequestParams.TABLE_NAME] = self.table_name
        return args
