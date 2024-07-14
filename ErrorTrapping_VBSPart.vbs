Option Explicit

' Head
Dim oAnsoftApp
Dim oDesktop
Dim oProject
Dim oDesign
Dim oEditor
Set oAnsoftApp = CreateObject("Ansoft.ElectronicsDesktop")
Set oDesktop = oAnsoftApp.GetAppDesktop()
oDesktop.RestoreWindow
Set oProject = oDesktop.SetActiveProject("220_Zhengti")
Set oDesign = oProject.SetActiveDesign("HFSSDesign1")
Set oEditor = oDesign.SetActiveEditor("3D Modeler")

Dim messageList
messageList = oDesktop.GetMessages("220_Zhengti", "HFSSDesign1", 2)

Dim objShell, pythonScript, inputString, outputFile, command, fso, file, result
Set objShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

' 定义python对象，输入对象，输出对象
pythonScript = "C:\PythonProject\ErrorTrapping_PythonPart.py"
inputString = messageList
outputFile = "C:\VBSProject\ErrorTrapping\output.txt"

' 构造调用Python脚本的命令，包括输入字符串和输出文件
command = "python """ & pythonScript & """ """ & inputString & """ """ & outputFile & """"

' 执行命令
objShell.Run command, 0, True

' 读取输出文件内容
If fso.FileExists(outputFile) Then
    Set file = fso.OpenTextFile(outputFile, 1)
    result = file.ReadAll()
    file.Close
    WScript.Echo result
Else
    WScript.Echo "Output file not found."
End If

Set objShell = Nothing
Set fso = Nothing
Set file = Nothing