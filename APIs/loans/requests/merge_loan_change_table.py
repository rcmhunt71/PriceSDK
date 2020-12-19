from dataclasses import dataclass

from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class MergeLoanChangeTableRequestParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberID"
    FANNIE_FILE: str = "FannieFile"
    DIFFERENCE_XML: str = "DifferenceXML"


class MergeLoanChangeTableRequest(SimpleRequestModel):
    def __init__(self, loan_number_id, fannie_file, difference_xml, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.fannie_file = fannie_file
        self.difference_xml = difference_xml
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[MergeLoanChangeTableRequestParams.LOAN_NUMBER_ID] = self.loan_number_id
        args[MergeLoanChangeTableRequestParams.FANNIE_FILE] = self.fannie_file
        args[MergeLoanChangeTableRequestParams.DIFFERENCE_XML] = self.difference_xml
        return args
