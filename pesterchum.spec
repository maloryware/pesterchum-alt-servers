# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['pesterchum.py'],
             pathex=['C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86', 'd:\\Documents\\PchumAttempt\\qt5\\pesterchum-alt-servers'],
             binaries=[('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-core-console-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-core-console-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-core-console-l1-2-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-core-datetime-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-core-debug-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-core-errorhandling-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-core-file-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-core-file-l1-2-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-core-file-l2-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-core-handle-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-core-heap-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-core-interlocked-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-core-libraryloader-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-core-localization-l1-2-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-core-memory-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-core-namedpipe-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-core-processenvironment-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-core-processthreads-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-core-processthreads-l1-1-1.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-core-profile-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-core-rtlsupport-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-core-string-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-core-synch-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-core-synch-l1-2-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-core-sysinfo-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-core-timezone-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-core-util-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\API-MS-Win-core-xstate-l2-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-crt-conio-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-crt-convert-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-crt-environment-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-crt-filesystem-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-crt-heap-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-crt-locale-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-crt-math-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-crt-multibyte-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-crt-private-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-crt-process-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-crt-runtime-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-crt-stdio-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-crt-string-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-crt-time-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\api-ms-win-crt-utility-l1-1-0.dll', '.'), ('C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\10.0.19041.0\\ucrt\\DLLs\\x86\\ucrtbase.dll', '.')],
             datas=[('quirks', 'quirks'), ('smilies', 'smilies'), ('themes', 'themes'), ('docs', 'docs'), ('README.md', '.'), ('LICENSE', '.'), ('CHANGELOG.md', '.'), ('PCskins.png', '.'), ('Pesterchum.png', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['collections.sys', 'collections._sre', 'collections._json', 'collections._locale', 'collections._struct', 'collections.array', 'collections._weakref', 'PyQt5.QtMultimedia', 'PyQt5.QtDBus', 'PyQt5.QtDeclarative', 'PyQt5.QtHelp', 'PyQt5.QtNetwork', 'PyQt5.QtSql', 'PyQt5.QtSvg', 'PyQt5.QtTest', 'PyQt5.QtWebKit', 'PyQt5.QtXml', 'PyQt5.QtXmlPatterns', 'PyQt5.phonon', 'PyQt5.QtAssistant', 'PyQt5.QtDesigner', 'PyQt5.QAxContainer'],
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
          name='Pesterchum',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='pesterchum.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=['qwindows.dll', 'qwindows.dll', 'Qt5Core.dll', 'qt5core.dll', 'Qt5Gui.dll', 'qt5gui.dll', 'vcruntime140.dll', 'vcruntime140.dll', 'MSVCP140.dll', 'msvcp140.dll', 'MSVCP140_1.dllapi-ms-win-core-console-l1-1-0.dll', 'msvcp140_1.dllapi-ms-win-core-console-l1-1-0.dll', 'api-ms-win-core-console-l1-1-0.dll', 'api-ms-win-core-console-l1-1-0.dll', 'api-ms-win-core-console-l1-2-0.dll', 'api-ms-win-core-console-l1-2-0.dll', 'api-ms-win-core-datetime-l1-1-0.dll', 'api-ms-win-core-datetime-l1-1-0.dll', 'api-ms-win-core-debug-l1-1-0.dll', 'api-ms-win-core-debug-l1-1-0.dll', 'api-ms-win-core-errorhandling-l1-1-0.dll', 'api-ms-win-core-errorhandling-l1-1-0.dll', 'api-ms-win-core-file-l1-1-0.dll', 'api-ms-win-core-file-l1-1-0.dll', 'api-ms-win-core-file-l1-2-0.dll', 'api-ms-win-core-file-l1-2-0.dll', 'api-ms-win-core-file-l2-1-0.dll', 'api-ms-win-core-file-l2-1-0.dll', 'api-ms-win-core-handle-l1-1-0.dll', 'api-ms-win-core-handle-l1-1-0.dll', 'api-ms-win-core-heap-l1-1-0.dll', 'api-ms-win-core-heap-l1-1-0.dll', 'api-ms-win-core-interlocked-l1-1-0.dll', 'api-ms-win-core-interlocked-l1-1-0.dll', 'api-ms-win-core-libraryloader-l1-1-0.dll', 'api-ms-win-core-libraryloader-l1-1-0.dll', 'api-ms-win-core-localization-l1-2-0.dll', 'api-ms-win-core-localization-l1-2-0.dll', 'api-ms-win-core-memory-l1-1-0.dll', 'api-ms-win-core-memory-l1-1-0.dll', 'api-ms-win-core-namedpipe-l1-1-0.dll', 'api-ms-win-core-namedpipe-l1-1-0.dll', 'api-ms-win-core-processenvironment-l1-1-0.dll', 'api-ms-win-core-processenvironment-l1-1-0.dll', 'api-ms-win-core-processthreads-l1-1-0.dll', 'api-ms-win-core-processthreads-l1-1-0.dll', 'api-ms-win-core-processthreads-l1-1-1.dll', 'api-ms-win-core-processthreads-l1-1-1.dll', 'api-ms-win-core-profile-l1-1-0.dll', 'api-ms-win-core-profile-l1-1-0.dll', 'api-ms-win-core-rtlsupport-l1-1-0.dll', 'api-ms-win-core-rtlsupport-l1-1-0.dll', 'api-ms-win-core-string-l1-1-0.dll', 'api-ms-win-core-string-l1-1-0.dll', 'api-ms-win-core-synch-l1-1-0.dll', 'api-ms-win-core-synch-l1-1-0.dll', 'api-ms-win-core-synch-l1-2-0.dll', 'api-ms-win-core-synch-l1-2-0.dll', 'api-ms-win-core-sysinfo-l1-1-0.dll', 'api-ms-win-core-sysinfo-l1-1-0.dll', 'api-ms-win-core-timezone-l1-1-0.dll', 'api-ms-win-core-timezone-l1-1-0.dll', 'api-ms-win-core-util-l1-1-0.dll', 'api-ms-win-core-util-l1-1-0.dll', 'API-MS-Win-core-xstate-l2-1-0.dll', 'api-ms-win-core-xstate-l2-1-0.dll', 'api-ms-win-crt-conio-l1-1-0.dll', 'api-ms-win-crt-conio-l1-1-0.dll', 'api-ms-win-crt-convert-l1-1-0.dll', 'api-ms-win-crt-convert-l1-1-0.dll', 'api-ms-win-crt-environment-l1-1-0.dll', 'api-ms-win-crt-environment-l1-1-0.dll', 'api-ms-win-crt-filesystem-l1-1-0.dll', 'api-ms-win-crt-filesystem-l1-1-0.dll', 'api-ms-win-crt-heap-l1-1-0.dll', 'api-ms-win-crt-heap-l1-1-0.dll', 'api-ms-win-crt-locale-l1-1-0.dll', 'api-ms-win-crt-locale-l1-1-0.dll', 'api-ms-win-crt-math-l1-1-0.dll', 'api-ms-win-crt-math-l1-1-0.dll', 'api-ms-win-crt-multibyte-l1-1-0.dll', 'api-ms-win-crt-multibyte-l1-1-0.dll', 'api-ms-win-crt-private-l1-1-0.dll', 'api-ms-win-crt-private-l1-1-0.dll', 'api-ms-win-crt-process-l1-1-0.dll', 'api-ms-win-crt-process-l1-1-0.dll', 'api-ms-win-crt-runtime-l1-1-0.dll', 'api-ms-win-crt-runtime-l1-1-0.dll', 'api-ms-win-crt-stdio-l1-1-0.dll', 'api-ms-win-crt-stdio-l1-1-0.dll', 'api-ms-win-crt-string-l1-1-0.dll', 'api-ms-win-crt-string-l1-1-0.dll', 'api-ms-win-crt-time-l1-1-0.dll', 'api-ms-win-crt-time-l1-1-0.dll', 'api-ms-win-crt-utility-l1-1-0.dll', 'api-ms-win-crt-utility-l1-1-0.dll', 'ucrtbase.dll', 'ucrtbase.dll'],
               name='Pesterchum')
