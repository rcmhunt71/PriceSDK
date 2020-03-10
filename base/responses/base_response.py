import pprint

from PRICE.logger.logging import Logger

log = Logger(added_depth=1)


class ModelKeyMismatch(Exception):
    pass


class BaseResponse:
    ADD_KEYS = None
    SUB_MODELS = None

    def __init__(self, keys=None, objs=None, **kwargs):
        self._VARS = []
        self._OBJS = []
        self.raw = kwargs.copy()
        self.model_name = self.__class__.__name__

        log.debug(f"Instantiating '{self.model_name}'")

        self._combine_args(keys=keys, objs=objs)
        log.debug(f"COMBINED PARAMETERS:\n\tself._VARS: {self._VARS}\n\tself._OBJS: {self._OBJS}")
        log.debug(f"ORIGINAL KWARGS:\n{pprint.pformat(kwargs)}\n")

        updated_kwargs = False
        if self.ADD_KEYS is not None:
            # If only adding KEYS & no MODELS (nested sub-objects), create a list of NONE models
            if self.SUB_MODELS is None:
                self.SUB_MODELS = [None for _ in range(len(self.ADD_KEYS))]

            # If ADD_KEYS and SUB_MODELS provided, the number per list MUST be the same.
            elif len(self.SUB_MODELS) != len(self.ADD_KEYS):
                log.debug(f"Key Mismatch: SUB_MODELS: {len(self.SUB_MODELS)}   ADD_KEYS: {len(self.ADD_KEYS)}")
                log.debug(f"SUB_MODELS: {self.SUB_MODELS}")
                log.debug(f"ADD_KEYS: {self.ADD_KEYS}")
                raise ModelKeyMismatch()

            # Number of ADD_KEYS and SUB_MODELS match, so if:
            # SUB_MODEL is None: add to KEYS to be added to base model obj.
            # SUB_MODEL is not None:
            #     * Instantiate sub_model object and add it to the kwargs
            #     * add to _OBJS to be added to base model object
            for key, model in zip(self.ADD_KEYS, self.SUB_MODELS):
                if key in kwargs and kwargs.get(key) is not None:
                    if model is not None:
                        data = kwargs.get(key)

                        if isinstance(data, list):
                            log.debug(f"Inserting '{model}' into '{key}' attribute with list {data}")
                            kwargs[key] = model(*data)
                        else:
                            log.debug(f"Inserting '{model}' into '{key}' attribute with dict {data}")
                            kwargs[key] = model(**data)

                        self._OBJS.append(key)
                        updated_kwargs = True
                    else:
                        self._VARS.append(key)

        # Add each sub_model object or keyword to the base model object, based on what is in the **kwargs dict.
        if updated_kwargs:
            log.debug(f"Updated KWARGS:\n{pprint.pformat(kwargs)}\n")

        for keyword, value in kwargs.items():
            if keyword in self._VARS or keyword in self._OBJS:
                setattr(self, keyword, value)
            else:
                quote = "'" if isinstance(value, str) else ''
                print(f"Unrecognized argument for '{self.__class__.__name__}': "
                      f"Keyword: '{keyword}' --> Value: {quote}{value}{quote}")

    def _combine_args(self, keys=None, objs=None):
        if keys is not None:
            self._VARS.extend(keys)
            self._VARS = list(set(self._VARS))

        if objs is not None:
            self._OBJS.extend(objs)
            self._OBJS = list(set(self._OBJS))

    def __str__(self):
        return pprint.pformat(self.raw)


class BaseListResponse(list):
    SUB_MODEL = None

    def __init__(self, *arg_list):
        super().__init__()
        self.model_name = self.__class__.__name__
        self.raw = arg_list[::]

        log.debug(f"KWARGS:\n{pprint.pformat(arg_list)}\n")
        self.extend([self.SUB_MODEL(**value_dict) for value_dict in arg_list])

    def __str__(self):
        return pprint.pformat(self.raw)
