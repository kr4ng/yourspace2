"""
Settings used by yourspace2 project.

This consists of the general produciton settings, with an optional import of any local
settings.
"""

# Import production settings.
from yourspace2.settings.production import *

# Import optional local settings.
try:
    from yourspace2.settings.local import *
except ImportError:
    pass