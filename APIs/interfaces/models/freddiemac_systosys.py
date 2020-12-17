from dataclasses import dataclass


@dataclass
class FreddieMacSysToSysKeys:
    RESPONSE_STRING: str = "ResponseString"
    RESPONSE: str = "Response"
    RESULT: str = "Result"
    MERGE_MESSAGE: str = "MergeMessage"
    MERGED: str = "Merged"
    REQUEST: str = "Request"
