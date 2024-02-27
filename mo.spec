# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['mo\\main.py'],
    pathex=['mo'],
    datas=[],
    binaries=[('D:\\Users\Kelvin_Wu\\AppData\Local\\anaconda3\\envs\\openvino\\Lib\\site-packages\\openvino\\libs\\openvino.dll', 'openvino\\libs'),
			  ('D:\\Users\Kelvin_Wu\\AppData\Local\\anaconda3\\envs\\openvino\\Lib\\site-packages\\openvino\\libs\\openvino_ir_frontend.dll', 'openvino\\libs'),
			  ('D:\\Users\Kelvin_Wu\\AppData\Local\\anaconda3\\envs\\openvino\\Lib\\site-packages\\openvino\\libs\\openvino_onnx_frontend.dll', 'openvino\\libs'),
			  ('D:\\Users\Kelvin_Wu\\AppData\Local\\anaconda3\\envs\\openvino\\Lib\\site-packages\\openvino\\libs\\openvino_tensorflow_frontend.dll', 'openvino\\libs'),
			  ('D:\\Users\Kelvin_Wu\\AppData\Local\\anaconda3\\envs\\openvino\\Lib\\site-packages\\openvino\\libs\\tbb12.dll', 'openvino\\libs')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='mo',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
	contents_directory='.'
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='mo',
)
