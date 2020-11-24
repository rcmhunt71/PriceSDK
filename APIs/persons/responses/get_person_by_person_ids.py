from APIs.persons.models.person_by_person_ids import PersonByPersonIDsKeys, PersonByPersonIDsList
from base.common.response import CommonResponse


class GetPersonByPersonIDsResponse(CommonResponse):
    _ADD_KEYS = [PersonByPersonIDsKeys.PERSONS]
    _SUB_MODELS = [PersonByPersonIDsList]
