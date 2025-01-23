Set WshShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")
currentDir = objFSO.GetParentFolderName(WScript.ScriptFullName)
batFilePath = currentDir & "\BocchiFM.bat"
WshShell.Run Chr(34) & batFilePath & Chr(34), 0, False
