JsOsaDAS1.001.00bplist00?Vscript_?(() => {
	const app = Application.currentApplication()
	app.includeStandardAdditions = true
	var filePath = $(app.pathTo(this).toString()).stringByDeletingLastPathComponent.js
	var baseFilePath = filePath
	filePath = filePath + "/tmp/attachments.json"
	pythonInterpreter = `source '${baseFilePath}/venv/bin/activate' && python3`

	function readFile(file) {
    	// Convert the file to a string
    	let fileString = file.toString()
 		
    	// Read the file and return its contents
    	return app.read(Path(fileString))
	}

	var files = JSON.parse(readFile(filePath))

	// Update the initial progress information
	var filesCount = files.length
	Progress.totalUnitCount = filesCount
	Progress.completedUnitCount = 0
	Progress.description = `Uploading ${filesCount} Attachments...`
	Progress.additionalDescription = "Preparing to process."
 
	for (i = 0; i < filesCount; i++) {
		var a = i + 1
    	// Update the progress detail
    	Progress.additionalDescription = `Uploading attachment ${a} of ${filesCount}`
	
		var theFile = JSON.stringify(files[i])
    	// Upload the attachment
		app.doShellScript(`${pythonInterpreter} '${baseFilePath}/upload.py' '${theFile}'`)
 
    	// Increment the progress
    	Progress.completedUnitCount = a
		if(i != (filesCount - 1)) {
			delay(2) // Delay to show progress
		}
}

	app.doShellScript(`${pythonInterpreter} '${baseFilePath}/create_share.py' && deactivate`)

	app.displayNotification("All uploaded", { withTitle: "Success"})
})()                              ?jscr  ??ޭ