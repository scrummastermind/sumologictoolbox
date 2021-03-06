# -*- mode: python -*-
import PyInstaller.config
PyInstaller.config.CONF['distpath'] = "dist\\windows"
block_cipher = None

added_files = [
    ( 'data/*', 'data' ),
    ( 'qtmodern', 'qtmodern' ),
    ( 'modules/*', 'modules' )
    ]


a = Analysis(['sumotoolbox.py'],
             pathex=['Z:\\Projects\\PycharmProjects\\sumologictoolbox'],
             binaries=[],
             datas=added_files,
             hiddenimports=['pkg_resources.py2_warn'],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             win_no_prefer_redirects=None,
             win_private_assemblies=None,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='sumotoolbox_windows',
          debug=False,
          strip=None,
          upx=True,
          console=False )
