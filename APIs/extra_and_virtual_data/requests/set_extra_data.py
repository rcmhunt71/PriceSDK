from dataclasses import dataclass

from base.common.models.request import SimpleRequestModel, BaseRequestModelKeys


@dataclass
class SetExtraDataRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    EXTRA_DATA_NAME: str = "ExtraDataName"
    EXTRA_DATA_VALUE: str = "ExtraDataValue"
    ROW_NUMBER_ID: str = "RowNumberID"


class SetExtraDataRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, extra_data_name, extra_data_value, row_number_id, session_id, nonce,
                 pretty_print):
        self.loan_number_id = loan_number_id
        self.extra_data_name = extra_data_name
        self.extra_data_value = extra_data_value
        self.row_number_id = row_number_id
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[SetExtraDataRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[SetExtraDataRequestParams.EXTRA_DATA_NAME] = self.extra_data_name
        args[SetExtraDataRequestParams.EXTRA_DATA_VALUE] = self.extra_data_value
        args[SetExtraDataRequestParams.ROW_NUMBER_ID] = self.row_number_id
        return args
