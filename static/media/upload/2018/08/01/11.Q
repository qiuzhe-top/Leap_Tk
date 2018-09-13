[General]
SyntaxVersion=2
BeginHotkey=121
BeginHotkeyMod=0
PauseHotkey=0
PauseHotkeyMod=0
StopHotkey=123
StopHotkeyMod=0
RunOnce=1
EnableWindow=
MacroID=4e903cbc-934d-4892-95e2-2e8e8e6735c8
Description=ÎÒµÄ½Å±¾1
Enable=1
AutoRun=0
[Repeat]
Type=0
Number=1
[SetupUI]
Type=2
QUI=
[Relative]
SetupOCXFile=
[Comment]

[Script]
Do

FindColorEx 939, 535, 970, 564, "6D7B85", 1, 0.9, intX, intY
If intX < 0 And intY < 0 Then 
FindColorEx 939, 535, 970, 564, "778BB2", 1, 0.9, intX, intY
End If

If intX < 0 And intY < 0 Then 
FindColorEx 939, 535, 970, 564, "C98F44", 1, 0.9, intX, intY
End If


If intX < 0 And intY < 0 Then 
FindColorEx 939, 535, 970, 564, "75433A", 1, 0.9, intX, intY
End If
If intX < 0 And intY < 0 Then 
FindColorEx 939, 535, 970, 564, "95ACDB", 1, 0.9, intX, intY
End If

If intX < 0 And intY < 0 Then 
FindColorEx 939, 535, 970, 564, "A75753", 1, 0.9, intX, intY
End If


If intX > 0 And intY > 0 Then 
//MoveTo intX, intY
LeftClick 1
Delay 30
LeftClick 1

End If

Loop

//6D7B85  778BB2