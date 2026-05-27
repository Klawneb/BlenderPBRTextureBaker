import importlib.util
from pathlib import Path


_ADDON_PATH = Path(__file__).with_name("Blender PBR Baker.py")
_SPEC = importlib.util.spec_from_file_location(f"{__name__}._addon", _ADDON_PATH)
_ADDON = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_ADDON)

register = _ADDON.register
unregister = _ADDON.unregister

