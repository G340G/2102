const btn = document.getElementById("generate");
const status = document.getElementById("status");
const video = document.getElementById("latest");

fetch("manifest.json")
.then(r=>r.json())
.then(data=>{
    video.src = data.latest;
});

btn.onclick = async () => {
    status.innerText = "SIGNAL REQUESTED...";
    await fetch("https://api.github.com/repos/YOUR_USERNAME/YOUR_REPO/dispatches", {
        method: "POST",
        headers: {
            "Accept": "application/vnd.github+json",
            "Authorization": "Bearer YOUR_GITHUB_TOKEN"
        },
        body: JSON.stringify({
            event_type: "generate_signal"
        })
    });
    status.innerText = "GENERATION IN PROGRESS...";
};
