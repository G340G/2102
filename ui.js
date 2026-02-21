const btn = document.getElementById("generate");
const status = document.getElementById("status");
const video = document.getElementById("latest");

fetch("manifest.json")
.then(r=>r.json())
.then(data=>{
    video.src = data.latest + "?t=" + Date.now();
})
.catch(()=>{
    video.style.display = "none";
});

btn.onclick = () => {
    status.innerText = "OPENING CONTROL PANEL...";
    window.open(
        "https://github.com/YOUR_USERNAME/YOUR_REPO/actions",
        "_blank"
    );
};
