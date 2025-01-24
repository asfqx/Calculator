[Setup]
AppName=Calculate_your_digits
AppVersion=1.0
DefaultDirName={pf}\Calculator
DefaultGroupName=Calculator
Compression=lzma
SolidCompression=yes

[Files]
Source: "C:\my_university_practics\5_semestr\git_luk2\task4\dist\calculator.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Calculate_your_digits"; Filename: "{app}\calculator.exe"
Name: "{group}\Uninstall_Calculate_your_digits"; Filename: "{uninstallexe}"