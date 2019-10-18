# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['mypaint.py'],
             pathex=['/Users/timh/local/mypaint/mypaint'],
             binaries=[
                 ('build/lib.macosx-10.14-x86_64-3.7/lib/_mypaintlib.cpython-37m-darwin.so', 'lib'),
                 ('../install/lib/libmypaint-2.0.0.dylib', '.'),
             ],
             datas=[
                 ('backgrounds', 'share/mypaint/backgrounds'),
                 ('palettes', 'share/mypaint/palettes'),
                 ('pixmaps', 'share/mypaint/pixmaps'),
                 ('../install/share/mypaint-data', 'share/mypaint-data'),
                 ('gui', 'gui'),
             ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='mypaint',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='mypaint')

app = BUNDLE(coll,
             name='MyPaint.app',
             icon='desktop/MyPaint.icns',
             bundle_identifier='org.mypaint.timmmm')
