import os
import sys


def setup():
    """Call this method to configure your WSGI application.

    Add any of your customs setup calls to this as well.
    """
    setup_lib_path()


def setup_lib_path():
    """Add lib to path."""
    libs_dir = os.path.join(os.path.dirname(__file__), 'lib')
    if libs_dir not in sys.path:
        sys.path.insert(0, libs_dir)
