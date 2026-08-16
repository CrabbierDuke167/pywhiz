"""
pywhiz - Fast, effortless, and friendly Python helper functions.
"""

__version__ = "0.1.6"

from .string_utils import (
    v_count,
    c_count,
    w_count,
    odd_count,
    even_count,
)

from .text_file_utils import (
    txt_wc,
    txt_w_pos,
)

from .list_utils import (
    unique,
    duplicates,
    compact,
    shuffle,
    sample,
    sample_one,
)
__all__ = [
    "v_count",
    "c_count",
    "w_count",
    "odd_count",
    "even_count",
    "txt_wc",
    "txt_w_pos",
    "unique",
    "duplicates",
    "compact",
    "shuffle",
    "sample",
    "sample_one",
]
