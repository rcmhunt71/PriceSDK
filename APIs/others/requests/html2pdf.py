from dataclasses import dataclass
from base.common.models.request import BaseRequestModelKeys, SimpleRequestModel


@dataclass
class HTML2PDFRequestParams(BaseRequestModelKeys):
    HTML: str = "HTML"
    ZOOM_FACTOR: str = "ZoomFactor"
    TIME_DELAY: str = "TimeDelay"
    PAPER_SIZE: str = "PaperSize"


class HTML2PDFRequest(SimpleRequestModel):
    def __init__(self, html, zoom_factor, time_delay, paper_size, session_id, nonce, pretty_print):
        self.html = html
        self.zoom_factor = zoom_factor
        self.time_delay = time_delay
        self.paper_size = paper_size
        super().__init__(session_id=session_id, nonce=nonce, pretty_print=pretty_print)

    def to_params(self):
        args = super().to_params()
        args[HTML2PDFRequestParams.HTML] = self.html
        args[HTML2PDFRequestParams.ZOOM_FACTOR] = self.zoom_factor
        args[HTML2PDFRequestParams.TIME_DELAY] = self.time_delay
        args[HTML2PDFRequestParams.PAPER_SIZE] = self.paper_size
        return args
