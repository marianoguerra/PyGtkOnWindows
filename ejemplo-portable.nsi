SetCompressor 'lzma'

Name 'ejemplo-portable.exe'
OutFile 'ejemplo-portable.exe'
SilentInstall silent

Section
	SetOutPath '$EXEDIR\Portable'
	File /r dist\*.*
	SetOutPath '$EXEDIR\Portable'
	nsExec::Exec $EXEDIR\Portable\ejemplo.exe
SectionEnd
