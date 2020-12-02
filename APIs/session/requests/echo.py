import pprint
import typing
from dataclasses import dataclass

from base.common.models.request import BaseRequestModel


@dataclass
class EchoRequestParams:
    MESSAGE: str = "Message"


class EchoRequest(BaseRequestModel):
    def __init__(self, payload_dict, session_id, nonce, pretty_print, **kwargs):
        self.kwargs = kwargs
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict, pretty_print=pretty_print)

    def build_payload(self) -> typing.Dict[str, typing.Any]:
        payload_items = {}

        for key in self.kwargs.keys():
            if getattr(EchoRequestParams, key.upper(), None) is not None:
                payload_items.update({getattr(EchoRequestParams, key.upper()): self.kwargs[key]})
                break

        return payload_items


if __name__ == '__main__':
    kwargs = {"messag": "skip", "meSSage": "print out", "Message": "do not write"}
    load = {"message": "payload text message"}

    res = EchoRequest(payload_dict=None, session_id=None, nonce=None, pretty_print=None, **kwargs)

    print("PAYLOAD:\n", pprint.pformat(res.payload))
