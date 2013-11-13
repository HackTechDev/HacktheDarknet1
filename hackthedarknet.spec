# -*- mode: python -*-
a = Analysis(['hackthedarknet.py'],
             pathex=['/home/solomonkane/PYTHON/HackTheDarkNet'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='hackthedarknet',
          debug=False,
          strip=None,
          upx=True,
          console=True )
