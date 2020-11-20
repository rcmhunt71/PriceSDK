from dataclasses import dataclass, fields
from base.responses.base_response import BaseResponse, BaseListResponse


@dataclass
class EmployeesInfoKeys:
    EMPLOYEE_ID: str = "EmployeeID"
    PERSON_ID: str = "PersonID"
    FIRST_NAME: str = "FirstName"
    MIDDLE_NAME: str = "MiddleName"
    LAST_NAME: str = "LastName"
    NO_LONGER_EMPLOYED: str = "NoLongerEmployed"
    LOCKOUT: str = "Lockout"
    EMPLOYEE_TYPE: str = "EmployeeType"
    EMAIL_ADDRESS: str = "EMailAddress"
    TITLE: str = "Title"
    VOICE: str = "Voice"
    CELL: str = "Cell"
    EXTENSION: str = "Extension"
    NMLS_ID: str = "NMLSID"
    LENDER_OFFICE_ID: str = "LenderOfficeID"


@dataclass
class EmployeesKeys:
    EMPLOYEES: str = "Employees"


class Employee(BaseResponse):
    _ADD_KEYS = [field.default for field in fields(EmployeesInfoKeys)]


class Employees(BaseListResponse):
    _SUB_MODEL = Employee
