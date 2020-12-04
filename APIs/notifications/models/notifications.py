from dataclasses import dataclass


@dataclass
class MergeEmailTemplateKeys:
    SUBJECT: str = "Subject"
    EMAIL_BODY: str = "EmailBody"


@dataclass
class SendEmailAndMakeConvLogKeys:
    MEMO_ID: str = "MemoID"
