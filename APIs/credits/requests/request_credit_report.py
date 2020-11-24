import pprint
from copy import copy
from dataclasses import dataclass, fields
from typing import Dict, Any

from base.common.models.request import SimpleRequestModel


@dataclass
class RequestCreditReportRequestParams:
    LOAN_NUMBER_ID: str = "LoanNumberID"
    RMCR: str = "RMCR"
    FM_DU_ID: str = "FMDUID"
    PRE_QUALIFICATION: str = "Prequalification"
    TRW: str = "TRW"
    BORROWER_ID_LIST: str = "BorrowerIDList"
    CBI: str = "CBI"
    USERNAME: str = "UserName"
    PASSWORD: str = "Password"
    CREDIT_COMPANY: str = "CreditCompany"
    TU: str = "TU"


class RequestCreditReportRequestParamsList:
    KEYS = [field.name.lower() for field in fields(RequestCreditReportRequestParams)]


class CreditCompany:
    FANNIE_MAE: str = "FannieMae"
    CBC: str = "CBC"
    CREDCO: str = "Credco"
    AVANTUS: str = "Avantus"
    EQUIFAX: str = "Equifax"
    FACTUAL_DATA: str = "Factual Data"
    KROLL_FACT: str = "KrollFact"
    MERIDIAN_LINK: str = "Meridian Link"
    SHARPER_LENDING: str = "Sharper Lending"


class RequestCreditReportRequest(SimpleRequestModel):

    def __init__(self, loan_number_id, rmcr, fm_du_id, pre_qualification, trw, borrower_id_list, cbi, username,
                 password, credit_company, tu, payload_dict, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        self.rmcr = rmcr
        self.fm_du_id = fm_du_id
        self.pre_qualification = pre_qualification
        self.trw = trw
        self.borrower_id_list = borrower_id_list
        self.cbi = cbi
        self.username = username
        self.password = password
        self.credit_company = credit_company
        self.tu = tu
        self.payload = payload_dict
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict, pretty_print=pretty_print)

    def to_params(self) -> Dict[str, Any]:
        """
            Payload takes priority over arguments.
            If both (argument and payload key) are supplied as an input,
            only payload key will be sent in the body of the request.
        """

        args = super().to_params()
        dict_params = copy(self.__dict__)
        list_keys = []

        if self.payload:
            list_keys = [key.lower() for key in self.payload.keys()]

        for key, value in dict_params.items():
            if key in RequestCreditReportRequestParamsList.KEYS:
                if key.replace('_', '') not in list_keys and value is None:
                    pass
                elif key.replace('_', '') not in list_keys:
                    args[getattr(RequestCreditReportRequestParams, key.upper())] = value

        return args


if __name__ == '__main__':
    kwargs = {
        # "RMCR": 0,
        "FMDUID": None,
        # "Prequalification": 0,
        "TRW": 0,
        "BorrowerIDList": None,
        "CBI": 0,
        "UserName": "Test",
        "LoanNumberID": 334400,
        "Password": 1234,
        "CreditCompany": CreditCompany.AVANTUS,
        "TU": 0
    }

    res = RequestCreditReportRequest(loan_number_id=None, rmcr=10, fm_du_id=10, pre_qualification=None, trw=None,
                                     borrower_id_list=None, cbi=11, username=None, password=None, credit_company=None,
                                     tu=None, payload_dict=kwargs, session_id=None, nonce=None, pretty_print=None)

    print("KWARGS:", res.as_params_dict)
    print("\nPAYLOAD:\n", pprint.pformat(res.payload))

    test = [_ for _ in res.as_params_dict.keys() if _ in res.payload]
    assert [] == test, "False, duplicated params found"
