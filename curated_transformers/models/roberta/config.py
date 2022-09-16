from dataclasses import dataclass

from ..bert import BertConfig


@dataclass
class RobertaConfig(BertConfig):
    # Same as BertConfig

    def __init__(self, *args, **kwargs):
        super(RobertaConfig, self).__init__(*args, **kwargs)