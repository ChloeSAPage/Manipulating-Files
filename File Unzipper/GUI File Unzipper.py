import PySimpleGUI as sg
import unzip
sg.theme("Random")

compress_ = [sg.Text("Select file to unzip:"), sg.Input(tooltip="Target file"), sg.FileBrowse("Choose", key = "file")]
destination_ = [sg.Text("Select file destination:"), sg.InputText(tooltip="File destination"), sg.FolderBrowse("Choose", key =  "folder")]
unzip_button = [sg.Button("Unzip"), sg.Text(key="output")]
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("File Unzipper", layout= [compress_, destination_, unzip_button])

while True:
    event, values = window.read()
    print(event, values)
    filepath = values["file"]
    dest_directory = values["folder"]
    unzip.unzip(filepath, dest_directory)
    window["output"].update(value="Extraction Complete")

window.close()