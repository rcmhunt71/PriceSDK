from dataclasses import dataclass

from base.clients.base_client import BaseClient

from APIs.data_checks.requests.evaluate_data_check_bundle import EvaluateDataCheckBundleRequest
from APIs.data_checks.responses.evaluate_data_check_bundle import EvaluateDataCheckBundleResponse


@dataclass
class ApiEndpoints:
    EVALUATE_DATA_CHECK_BUNDLE: str = "evaluate_data_check_bundle"


class DataChecksClient(BaseClient):

    def evaluate_data_check_bundle(self, loan_number_id, data_check_bundle_id, session_id=None, nonce=None,
                                   pretty_print=False):
        request_model = EvaluateDataCheckBundleRequest(loan_number_id=loan_number_id,
                                                       data_check_bundle_id=data_check_bundle_id,
                                                       session_id=self._get_session_id(session_id),
                                                       nonce=self._get_nonce(nonce), pretty_print=pretty_print)

        return self.get(resource_endpoint=ApiEndpoints.EVALUATE_DATA_CHECK_BUNDLE,
                        response_model=EvaluateDataCheckBundleResponse,
                        params=request_model.as_params_dict)
