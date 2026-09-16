#!/usr/bin/env python3
# Full game: https://github.com/ApacheAde/elbowos-chroma-games/blob/main/abyss_lure/abyss_lure.py
import runpy, urllib.request, tempfile, os, sys
URL = "https://raw.githubusercontent.com/ApacheAde/elbowos-chroma-games/main/abyss_lure/abyss_lure.py"
path = os.path.join(tempfile.gettempdir(), "abyss_lure_full.py")
try:
    urllib.request.urlretrieve(URL, path)
    runpy.run_path(path, run_name="__main__")
except Exception as e:
    print("Need network or local copy from elbowos-chroma-games/abyss_lure", e)
    sys.exit(1)
