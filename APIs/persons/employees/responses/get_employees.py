from APIs.persons.employees.models.employees import EmployeesKeys, Employees
from base.common.response import CommonResponse


class GetEmployeesResponse(CommonResponse):
    _ADD_KEYS = [EmployeesKeys.EMPLOYEES]
    _SUB_MODELS = [Employees]
