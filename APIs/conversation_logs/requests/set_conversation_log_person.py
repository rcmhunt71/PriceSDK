from typing import List, Dict, Any, Union
from dataclasses import dataclass
from base.common.models.request import KwargsRequestModel, DataKeys


@dataclass
class SetConversationLogPersonPayload:
    CONVERSATION_ID: str = "ConversationID"
    MEMO_ID: str = "MemoID"
    PERSON_ID: str = "PersonID"
    COPY_TYPE: str = "CopyType"
    FIELDS: str = "Fields"


@dataclass
class SetConversationLogPersonFieldNames:
    CONVERSATION_ID: str = "ConversationID"
    MEMO_ID: str = "MemoID"
    PERSON_ID: str = "PersonID"
    COPY_TYPE: str = "CopyType"
    VIEWED_ON_GMT: str = "ViewedOnGMT"
    HIDE: str = "Hide"
    PUSHBACK_REASON: str = "PushbackReason"
    PUSHBACK_DATE_TIME: str = "PushbackDateTime"
    ORDER_ID: str = "OrderID"
    RECEIPT_TYPE: str = "ReceiptType"
    SQL_CREATED_ON: str = "SQL_CreatedOn"
    SQL_MODIFIED_ON: str = "SQL_ModifiedOn"
    ACTION: str = "Action"


class SetConversationLogPersonRequest(KwargsRequestModel):
    data_payload = SetConversationLogPersonPayload
    REQUEST_PAYLOAD_KEY: str = "ConversationLogPerson"

    def __init__(self, payload_dict, session_id, nonce, pretty_print, **kwargs):
        super().__init__(session_id=session_id, nonce=nonce, payload=payload_dict, pretty_print=pretty_print, **kwargs)

    def build_payload(self) -> Dict[str, List[Dict[Any, Union[List[Dict[str, Any]], Any]]]]:
        payload_dict = {}
        for payload_key in self.attr_list:
            if getattr(self, payload_key.lower(), None) is not None:
                if payload_key.title() == SetConversationLogPersonPayload.FIELDS:
                    fields_list = []
                    for key, value in getattr(self, payload_key.lower()).items():
                        fields_list.append({DataKeys.FIELD_NAME: getattr(SetConversationLogPersonFieldNames,
                            key.upper(), key),
                            DataKeys.FIELD_VALUE: value})
                    payload_dict.update({SetConversationLogPersonPayload.FIELDS: fields_list})
                    continue
                payload_dict.update({getattr(self.data_payload, payload_key.upper(), payload_key):
                    getattr(self, payload_key.lower())})
        return {self.REQUEST_PAYLOAD_KEY: [payload_dict]}


if __name__ == "__main__":
    import pprint
    kwargs = {
        "ConversationID": 12345,
        "MemoID": 98765,
        "PersonID": 12345,
        "CopyType": 0,
        "Fields": {
            SetConversationLogPersonFieldNames.VIEWED_ON_GMT: "Yes",
            SetConversationLogPersonFieldNames.PUSHBACK_REASON: "Test",
            SetConversationLogPersonFieldNames.ACTION: "Yes",
            SetConversationLogPersonFieldNames.ORDER_ID: "123",
        }
    }
    print(f"KWARGS: {pprint.pformat(kwargs)}")
    obj = SetConversationLogPersonRequest(payload_dict=None, session_id=123456, nonce=123245687, pretty_print=False,
        **kwargs)
    print(f"\nPAYLOAD: {pprint.pformat(obj.payload)}")
    print("\nTesting SetConversationLogPersonRequest - payload_dict")
    obj_args = SetConversationLogPersonRequest(payload_dict=obj.payload, pretty_print=False, session_id=123456,
        nonce=123245687)
    print(f"PAYLOAD: {pprint.pformat(obj_args.payload)}")
