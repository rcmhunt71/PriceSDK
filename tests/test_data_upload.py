import unittest

from APIs.data_upload.models.data_upload import ProcessStringKeys, RegisterParameterSetKeys, UploadDataKeys
from APIs.data_upload.responses.process_string import ProcessStringResponse
from APIs.data_upload.responses.register_parameter_set import RegisterParameterSetResponse
from APIs.data_upload.responses.upload_data import UploadDataResponse
from tests.common.common_response_args import CommonResponseValidations, response_args

process_string_data = {
    ProcessStringKeys.DL_RESULT: "5345 Kietze Lane",
    ProcessStringKeys.LOAN_NUMBER_ID: 5538467,
    ProcessStringKeys.DATA_LANGUAGE: "(ihInfo(Employee,Loan_Officer_Id,GetFullAddress))"
}

parameter_keys_data = {
    RegisterParameterSetKeys.PARAMETER_SET_KEY: "ABFFDEC0019AEFF2347EC8009AEDA6438675309"
}

data_keys_data = {
    UploadDataKeys.TOKEN: "EC8009AEDA6438675309",
    UploadDataKeys.VALID_UNTIL: "2017-01-18T06:39:20.528"
}


class TestDataUpload(unittest.TestCase, CommonResponseValidations):
    def test_ProcessString_response(self):
        process_string_args = response_args.copy()
        process_string_args.update(process_string_data)
        process_string_resp = ProcessStringResponse(**process_string_args)
        self._validate_response(model=process_string_resp, model_data=process_string_args)

    def test_RegisterParameterSet_response(self):
        parameter_keys_args = response_args.copy()
        parameter_keys_args.update(parameter_keys_data)
        param_keys_model = RegisterParameterSetResponse(**parameter_keys_args)

        self._validate_response(model=param_keys_model, model_data=parameter_keys_args)

    def test_UploadData_response(self):
        upload_data_args = response_args.copy()
        upload_data_args.update(data_keys_data)
        upload_data_model = UploadDataResponse(**upload_data_args)

        self._validate_response(model=upload_data_model, model_data=upload_data_args)


if __name__ == '__main__':
    unittest.main()
