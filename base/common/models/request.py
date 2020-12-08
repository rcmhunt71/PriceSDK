import os
import typing
from abc import ABC, abstractmethod
from dataclasses import dataclass, fields
import json


@dataclass
class DataPayload:
    pass


@dataclass
class BaseRequestModelKeys:
    SESSION_ID: str = "SessionID"
    NONCE: str = "Nonce"
    PRETTY_PRINT: bool = "PrettyPrint"


@dataclass
class LoanNumberIdRequestModelParams(BaseRequestModelKeys):
    LOAN_NUMBER_ID: str = "LoanNumberId"


@dataclass
class DataKeys:
    FIELD_NAME: str = "FieldName"
    FIELD_VALUE: str = "FieldValue"


class BaseRequestModel(ABC):
    def __init__(self, session_id, nonce, payload=None, pretty_print=False):
        self.session_id = session_id
        self.nonce = nonce
        self.pretty_print = pretty_print
        self.as_params_dict = self.to_params()
        self.payload = payload if payload is not None else self.build_payload()
        self.as_json = self.to_json()

    def to_params(self):
        args = {
            BaseRequestModelKeys.SESSION_ID: self.session_id,
            BaseRequestModelKeys.NONCE: self.nonce,
        }
        if self.pretty_print:
            args[BaseRequestModelKeys.PRETTY_PRINT] = self.pretty_print
        return args

    def to_json(self):
        return json.dumps(self.payload) if type(self.payload) is not str else self.payload

    @abstractmethod
    def build_payload(self):
        pass


class KwargsRequestModel(BaseRequestModel):
    @property
    @abstractmethod
    def data_payload(self) -> dataclass:
        pass

    @property
    @abstractmethod
    def REQUEST_PAYLOAD_KEY(self) -> str:
        pass

    def __init__(self, session_id, nonce, payload=None, pretty_print=False, **kwargs):
        # Kwargs are key/value pairs where a key can be a lower-case SetLoanDataPayload attribute
        # e.g. -  SUB_FINANCE_HELOC_AMOUNT -->> sub_finance_heloc_amount

        # Dynamically set all attributes based kwargs that match a DataPayload attribute
        valid_keys = [elem.name for elem in fields(self.data_payload)]
        self.attr_list = []

        # Iterate through the kwargs
        for attr in kwargs.keys():

            # If kwargs.UPPER() matches a DataPayload attribute, create a model attribute and store the value.
            # Also record the name of the attribute for more efficient payload generation
            if attr.upper() in valid_keys or os.environ.get('TEST_ENV'):
                setattr(self, attr.lower(), kwargs[attr])
                self.attr_list.append(attr)

        super().__init__(session_id=session_id, nonce=nonce, payload=payload, pretty_print=pretty_print)

    def build_payload(self) -> typing.Dict[str, typing.List[typing.Dict[str, typing.Any]]]:
        payload_list = []

        # For all recorded dynamically created attributes, create a dual entry dictionary:
        # { FIELD_NAME: attr_name, FIELD_VALUE: attr_value }
        for payload_key in self.attr_list:
            if getattr(self, payload_key.lower(), None) is not None:
                payload_list.append(
                    {DataKeys.FIELD_NAME: getattr(self.data_payload, payload_key.upper(), payload_key),
                     DataKeys.FIELD_VALUE: getattr(self, payload_key.lower())})
        payload = {self.REQUEST_PAYLOAD_KEY: payload_list}
        return payload


class SimpleRequestModel(BaseRequestModel):
    def build_payload(self):
        return {}


class LoanNumberIdRequestModel(SimpleRequestModel):
    def __init__(self, loan_number_id, session_id, nonce, pretty_print):
        self.loan_number_id = loan_number_id
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[LoanNumberIdRequestModelParams.LOAN_NUMBER_ID] = self.loan_number_id
        return args
