import os

from distutils.core import setup, Extension

if os.name == 'nt':
	import py2exe

	opts = {
		'py2exe': {
			'packages': ['encodings', 'gtk'],
			'includes': ['locale', 'gio', 'cairo', 'pangocairo', 'pango',
				'atk', 'gobject', 'os', 'code', 'winsound', 'win32api',
				'win32gui', 'optparse'],
			'excludes': ['ltihooks', 'pywin', 'pywin.debugger',
				'pywin.debugger.dbgcon', 'pywin.dialogs',
				'pywin.dialogs.list', 'Tkconstants', 'Tkinter', 'tcl'
				'doctest', 'macpath', 'pdb', 'cookielib', 'ftplib',
				'pickle', 'caledar', 'win32wnet', 'unicodedata',
				'getopt', 'gdk'],
			'dll_excludes': ['libglade-2.0-0.dll', 'w9xpopen.exe'],
			'optimize': '2',
			'dist_dir': './dist',
		}
	}

	files = ['winlogo.gif', 'dlls/Microsoft.VC90.CRT.manifest',
			'dlls/msvcm90.dll',
			'dlls/msvcp90.dll',
			'dlls/msvcr71.dll',
			'dlls/msvcr90.dll']

	setup(
		name="ejemplo",
		version="1.0",
		description="an example for PyConAr 2010",
		author 		= "Mariano Guerra",
		author_email	= "luismarianoguerra@gmail.com",
		url		= "http://marianoguerra.com.ar",
		license		= "GNU GPL 2",
		requires	= ["gtk"],
		windows		= [{"script": "ejemplo.py", "dest_base": "ejemplo"}], # XXX
		console		= [{"script": "ejemplo.py", "dest_base": "ejemplo_debug"}], # XXX
		options		= opts,
		data_files	= files)

	print "done! files at: dist"

else:
	print "setup not implemented for", os.name
