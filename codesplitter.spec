# -*- mode: python ; coding: utf-8 -*-
import os
import sys
from kivy_deps import sdl2, glew
from PyInstaller.utils.hooks import collect_data_files

base_path = os.path.dirname(os.path.abspath(sys.argv[0]))

a = Analysis(
    [os.path.join(base_path, 'codesplitter.py')],
    pathex=[base_path],
    binaries=[],
    datas=[(os.path.join(base_path, 'codesplitter.ico'), 'image')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='codesplitter',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=os.path.join(base_path, 'codesplitter.ico'),
)
coll = COLLECT(
    exe, Tree(base_path),
    a.binaries,
    a.zipfiles,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    strip=False,
    upx=True,
    upx_exclude=[],
    name='codesplitter',
    icon=os.path.join(base_path, 'codesplitter.ico'),
)
