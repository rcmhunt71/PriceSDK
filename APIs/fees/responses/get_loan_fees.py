from APIs.fees.models.loan_fees import LoanFeeKeys
from base.common.models.data_table_response import DataTable
from base.common.response import CommonResponse


class GetLoanFeesResponse(CommonResponse):

    def __init__(self, **kwargs):
        key = LoanFeeKeys.LOAN_FEES
        model = DataTable

        self._OBJS = [key]
        self._combine_args(objs=self._OBJS)

        if kwargs.get(key, {}):
            kwargs[key] = model(**kwargs.get(key, {}))
        super().__init__(keys=None, objs=self._OBJS, **kwargs)
