"""
pywhiz - Fast, effortless, and friendly Python helper functions.
"""

__version__ = "0.1.4"

from .string_utils import (
    v_count,
    c_count,
    w_count,
    odd_count,
    even_count,
)

from .text_file_utils import (
    countf,
    positionf,
)

__all__ = [
    "v_count",
    "c_count",
    "w_count",
    "odd_count",
    "even_count",
    "countf",
    "positionf",
]
