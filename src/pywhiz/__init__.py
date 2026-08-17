"""
pywhiz - Fast, effortless, and friendly Python helper functions.
"""

__version__ = "0.1.8"

# fixed: 'not accessed' warning  
from .geo_utils import perim_square as perim_square
from .time_utils import t_countdown as t_countdown

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

from .num_utils import (
    is_prime,
    is_armstrong,
    fibonacci,
    hcf,
    lcm,
)

from .time_utils import (
    start_timer,
    end_timer,
    t_delay,
    t_countdown,
)

from .geo_utils import (
    perim_square,
    perim_rect,
    perim_tri,
    circum_circle,
    perim_polygon,
    area_square,
    area_rect,
    area_tri_base,
    area_tri_herons,
    area_circle,
    area_rhombus,
    area_trapezium,
    sa_cube,
    sa_cuboid,
    sa_cylinder,
    sa_cone,
    sa_sphere,
    sa_hemisphere,
    vol_cube,
    vol_cuboid,
    vol_cylinder,
    vol_cone,
    vol_sphere,
    vol_hemisphere,
)

from .csv_utils import (
    max_csv,
    min_csv,
    csv_summary,
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
    "is_prime",
    "is_armstrong",
    "fibonacci",
    "hcf",
    "lcm",
    "start_timer",
    "end_timer",
    "t_delay",
    "t_countdown"
    "perim_square",
    "perim_rect",
    "perim_tri",
    "circum_circle",
    "perim_polygon",
    "area_square",
    "area_rect",
    "area_tri_base",
    "area_tri_herons",
    "area_circle",
    "area_rhombus",
    "area_trapezium",
    "sa_cube",
    "sa_cuboid",
    "sa_cylinder",
    "sa_cone",
    "sa_sphere",
    "sa_hemisphere",
    "vol_cube",
    "vol_cuboid",
    "vol_cylinder",
    "vol_cone",
    "vol_sphere",
    "vol_hemisphere",
    "max_csv",
    "min_csv",
    "csv_summary",
]

