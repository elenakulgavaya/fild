import warnings

# pylint: disable=wrong-import-position
warnings.warn(
    "fild is deprecated and will no longer be maintained. "
    "Migrate to surety: pip install surety. "
    "Replace 'from fild.sdk import ...' with 'from surety import ...'. "
    "See https://github.com/elenakulgavaya/surety for details.",
    DeprecationWarning,
    stacklevel=2,
)

from .array import Array, Set
from .field import Field
from .dictionary import Dictionary
from .types import (
    Bool, Int, DateTime, Decimal, Enum, Float, Raw, String, StringDecimal,
    Uuid,
)
