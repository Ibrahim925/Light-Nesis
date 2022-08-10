const runButton = document.getElementById("run-button")

runButton.onclick = () => {
	const video = document.getElementById("video")
	const direction = document.getElementById("direction-select").value
	const participant = document.getElementById("participant-number-input").value
	const run = document.getElementById("run-input").value
	const sex = document.getElementById("sex-select").value

	if (!participant || participant < 1 || participant % 1 != 0) {
		return setMessage("Please set the participant to a positive integer!")
	} else if (!run || run < 1 || run % 1 != 0) {
		return setMessage("Please set the run to a positive integer!")
	} else if (sex == "Select") {
		return setMessage("Please set the sex!")
	} else if (direction == "Select") {
		return setMessage("Please select the direction!")
	} 
	
	video.src = "../../prompts/" + direction + ".mp4";
	video.play();

	const data = {
		run,
		sex,
		participant,
		direction
	}

	fetch("http://localhost:3000", {
		method: "POST",
		mode: "cors",
		headers: {
			"Content-Type": "application/json"
		},
		body: JSON.stringify(data),
	}).then((res) => {
		return res.json()
	}).then(data => {
		if (data.message) {
			setMessage(data.message)
		} else {
			setMessage("Streaming ended. Data collected successfully!")
		}
	})
}

function setMessage(message) {
	const messageEl = document.createElement("p")
	const text = document.createTextNode(message)
	messageEl.appendChild(text)
	const inputs = document.getElementById("inputs")
	inputs.removeChild(inputs.lastChild)
	inputs.appendChild(messageEl)
}
