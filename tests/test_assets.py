import unittest
from random import randrange, choice

from APIs.assets.models.assets import AssetsKeys, Assets, AssetInfoKeys, Asset
from APIs.assets.models.automobile import AutomobileKeys
from APIs.assets.responses.add_automobile import AddAutomobileResponse
from APIs.assets.responses.get_assets import GetAssetsResponse
from logger.logging import Logger
from tests.common.common_response_args import CommonResponseValidations, response_args

log = Logger()


# ---------------------------------------------------------------
#     ASSET TEST DATA
# ---------------------------------------------------------------
booleans = [True, False]
details = ['Yadda', 'Blah', 'Nope']
number_of_assets = 3


def build_asset():
    return {
        AssetInfoKeys.CUSTOMER_ID: randrange(999999),
        AssetInfoKeys.ASSET_ID: f"A-{randrange(999999)}",
        AssetInfoKeys.ASSET_NAME: f"TestAsset_{randrange(9)}",
        AssetInfoKeys.ASSET_TYPE: "Test",
        AssetInfoKeys.MARKET_VALUE: f"{randrange(99999)}",
        AssetInfoKeys.FIX_DESCRIPTION: "Broken",
        AssetInfoKeys.INSURANCE_FACE_VALUE: f"{randrange(99999)}",
        AssetInfoKeys.VERIFY: choice(booleans),
        AssetInfoKeys.VERIFY_DATE: f"{randrange(1990, 2019)}{randrange(1,12):02}{randrange(1,28):02}",
        AssetInfoKeys.BOTH: choice(booleans),
        AssetInfoKeys.LIQUID: choice(booleans),
        AssetInfoKeys.RETIREMENT_FUND_DETAIL: "{0}-{0}-{0}".format(choice(details))}


assets_list = [build_asset() for _ in range(number_of_assets)]


# ---------------------------------------------------------------
#   ASSET TESTS
# ---------------------------------------------------------------
class TestAssets(unittest.TestCase, CommonResponseValidations):
    def test_asset_model(self):
        asset_obj = Asset(**assets_list[0])
        self._validate_response(model=asset_obj, model_data=assets_list[0])

    def test_assets_model(self):
        self._test_assets_model(model=Assets(*assets_list), keys=assets_list[0].keys())

    def test_assets_response(self):
        assets_args = response_args.copy()
        assets_args[AssetsKeys.ASSETS] = assets_list
        assets_list_resp = GetAssetsResponse(**assets_args)

        self._verify(
            descript=f"{assets_list_resp}: Has {AssetsKeys.ASSETS}",
            actual=hasattr(assets_list_resp, AssetsKeys.ASSETS), expected=True)

        model = getattr(assets_list_resp, AssetsKeys.ASSETS)
        self._test_assets_model(model=model, keys=assets_list[0].keys())
        self._validate_response(model=assets_list_resp, model_data=assets_args)

    def test_automobile_response(self):
        key = AutomobileKeys.AUTOMOBILE_ID

        automobile_args = response_args.copy()
        automobile_args[key] = f"CAR-{randrange(999):03}"
        auto = AddAutomobileResponse(**automobile_args)

        self._validate_response(model=auto, model_data=automobile_args)

    def _test_assets_model(self, model, keys):
        self.assertEqual(len(assets_list), len(model))
        for index, asset in enumerate(assets_list):
            for key in keys:
                self._verify(
                    descript=f"{model[index].model_name} - Element #{index}: '{key}' are equal",
                    actual=getattr(model[index], key), expected=assets_list[index][key])


if __name__ == "__main__":
    unittest.main()
