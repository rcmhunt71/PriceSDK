from APIs.loans.models.final_value import FinalValueFieldsKeys, FinalValueScreenKeys
from base.common.response import CommonResponse


class GetFinalValueTagsResponse(CommonResponse):
    _ADD_KEYS = [FinalValueScreenKeys.FINAL_VALUE_SCREEN, FinalValueFieldsKeys.FINAL_VALUE_FIELD]
    _SUB_MODELS = [None, None]

    def get_final_value_screens(self):
        return getattr(self, FinalValueScreenKeys.FINAL_VALUE_SCREEN)

    def get_final_value_fields(self):
        return getattr(self, FinalValueFieldsKeys.FINAL_VALUE_FIELD)
