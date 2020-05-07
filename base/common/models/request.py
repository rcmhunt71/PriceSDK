from abc import ABC, abstractmethod
from dataclasses import dataclass
import json


@dataclass
class BaseRequestModelKeys:
    SESSION_ID: str = "SessionID"
    NONCE: str = "Nonce"
    PRETTY_PRINT: bool = "PrettyPrint"


class BaseRequestModel(ABC):
    def __init__(self, session_id, nonce, payload=None, pretty_print=False):
        self.session_id = session_id
        self.nonce = nonce
        self.pretty_print = pretty_print
        self.as_params_dict = self.to_params()
        self.as_json = self.to_json()
        self.payload = payload if payload is not None else self.build_payload()

    def to_params(self):
        args = {
            BaseRequestModelKeys.SESSION_ID: self.session_id,
            BaseRequestModelKeys.NONCE: self.nonce,
        }
        if self.pretty_print:
            args[BaseRequestModelKeys.PRETTY_PRINT] = self.pretty_print
        return args

    def to_json(self):
        return json.dumps(self.to_params())

    @abstractmethod
    def build_payload(self):
        return {}
