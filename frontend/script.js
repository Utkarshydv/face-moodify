const webcam = document.getElementById("webcam");
const detectBtn = document.getElementById("detectBtn");
const emotionText = document.getElementById("emotionText");
const songsContainer = document.getElementById("songsContainer");

navigator.mediaDevices.getUserMedia({ video: true }).then(stream => {
  webcam.srcObject = stream;
}).catch(console.error);

const emojiMap = { happy: "😄", sad: "😢", angry: "😠", neutral: "😐" };

detectBtn.onclick = async () => {
  emotionText.textContent = "⏳ Detecting...";
  songsContainer.innerHTML = "";

  const canvas = document.createElement("canvas");
  canvas.width = webcam.videoWidth;
  canvas.height = webcam.videoHeight;
  canvas.getContext("2d").drawImage(webcam, 0, 0);

  const res = await fetch("http://127.0.0.1:5000/detect", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ image: canvas.toDataURL("image/jpeg") })
  }).then(r => r.json());

  const emotion = res.emotion;
  emotionText.textContent = `Your mood is ${emotion.toUpperCase()} ${emojiMap[emotion] || ""}`;

  res.songs.slice(0,3).forEach(song => {
    const card = document.createElement("div");
    card.className = "song-card";
    card.onclick = () => window.open(song.link, "_blank");
    card.innerHTML = `
      <img src="${song.cover}" alt="${song.title}"/>
      <div class="song-info">
        <p class="song-title">${song.title}</p>
        <p class="artist-name">${song.artist}</p>
      </div>`;
    songsContainer.appendChild(card);
  });
};
