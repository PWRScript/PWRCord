# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# Library Imports
# -----------------------------------------------------------------------------
from typing import Any, Callable, Coroutine

# -----------------------------------------------------------------------------
# Type defs
# -----------------------------------------------------------------------------
AsyncFunction = Callable[..., Coroutine[Any, Any, Any]]
"""async def compatible function"""

# -----------------------------------------------------------------------------
# Exports
# -----------------------------------------------------------------------------
__all__ = ["AsyncFunction"]
