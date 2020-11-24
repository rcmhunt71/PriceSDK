from random import choice, randrange
import unittest

from APIs.passwords.models.password import ForceChangePasswordKeys, PasswordAgeKeys
from APIs.passwords.responses.check_for_force_change_password import CheckForForceChangePasswordResponse
from APIs.passwords.responses.get_employee_password_age import GetEmployeePasswordAge
from tests.common.common_response_args import CommonResponseValidations, response_args

booleans = [True, False]


class TestChangePassword(unittest.TestCase, CommonResponseValidations):
    def test_CheckForForceChangePassword(self):
        model_args = response_args.copy()
        model_args[ForceChangePasswordKeys.FORCE_CHANGE_PASSWORD] = choice(booleans)
        response = CheckForForceChangePasswordResponse(**model_args)
        self._validate_response(model=response, model_data=model_args)

    def test_GetEmployeePasswordAge(self):
        expires_in = randrange(365)
        password_age_args = {
            PasswordAgeKeys.EXPIRY_NOTICE_IN_DAYS: expires_in,
            PasswordAgeKeys.DAYS_REMAINING: expires_in - 7,
            PasswordAgeKeys.EXPIRES: choice(booleans)
        }

        model_args = response_args.copy()
        model_args.update(password_age_args)
        response = GetEmployeePasswordAge(**model_args)
        self._validate_response(model=response, model_data=model_args)


if __name__ == '__main__':
    unittest.main()
