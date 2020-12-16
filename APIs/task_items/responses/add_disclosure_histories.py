from base.common.response import CommonResponse


class AddDisclosureHistoriesKeys:
    DISCLOSURE_EVENT_ID: str = "DisclosureEventID"


class AddDisclosureHistoriesResponse(CommonResponse):
    _ADD_KEYS = [AddDisclosureHistoriesKeys.DISCLOSURE_EVENT_ID]
    _SUB_MODELS = [None]
