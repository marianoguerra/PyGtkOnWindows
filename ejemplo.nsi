; ejemplo.nsi

Name "ejemplo loco"
OutFile "ejemplo-install.exe"
SetCompressor /SOLID lzma
InstallDir $PROGRAMFILES\ejemplo

InstallDirRegKey HKLM "Software\ejemploloco" "Install_Dir"

Section "ejemplo"

	SectionIn RO

	SetOutPath $INSTDIR

	File /r dist\*.*

	WriteRegStr HKLM SOFTWARE\ejemploloco "Install_Dir" "$INSTDIR"

SectionEnd

Section "Start Menu Shortcuts"

	CreateDirectory "$SMPROGRAMS\ejemplo"
	CreateShortCut "$SMPROGRAMS\ejemplo\ejemplo.lnk" "$INSTDIR\ejemplo.exe" "" "$INSTDIR\ejemplo.exe" 0
	CreateShortCut "$SMPROGRAMS\ejemplo\ejemplodebug.lnk" "$INSTDIR\ejemplo.exe" "" "$INSTDIR\ejemplo_debug.exe" 0

SectionEnd
