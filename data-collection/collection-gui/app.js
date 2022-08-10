const directionSelector = document.getElementById("direction-select")

directionSelector.onchange = (event) => {
	const direction = event.target.value;
	const video = document.getElementById("video")
	const participant = document.getElementById("participant-number-input").value
	const run = document.getElementById("run-input").value
	const sex = document.getElementById("sex-select").value
	
	video.src = "../prompts/" + direction + ".mp4";
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
		console.log(data)
	})
}
