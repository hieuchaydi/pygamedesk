[Setup]
AppName=sk
AppVersion=3.0
DefaultDirName={pf}\hieuadmin
OutputDir=.\Output
OutputBaseFilename=Setup
Compression=lzma
SolidCompression=yes

[Files]
Source: "C:\Users\FPT\OneDrive\Desktop\pygame\dist\gaming.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\FPT\OneDrive\Desktop\pygame\media\tree.png"; DestDir: "{app}\media"; Flags: ignoreversion

[Icons]
Name: "{group}\Snake Game"; Filename: "{app}\gaming.exe"
Name: "{userdesktop}\Snake Game"; Filename: "{app}\gaming.exe"

[Registry]
Root: HKCU; Subkey: "Software\Snake Game"; ValueType: string; ValueName: "InstallPath"; ValueData: "{app}"; Flags: uninsdeletevalue
