// ===============================
// GLOBAL VARIABLES
// ===============================
let selectedFile = null;
let lastSpeech = null;

// ===============================
// FILE INPUT HANDLING
// ===============================
const cameraInput = document.getElementById("cameraInput");
const galleryInput = document.getElementById("galleryInput");
const preview = document.getElementById("preview");

cameraInput.addEventListener("change", handleFile);
galleryInput.addEventListener("change", handleFile);

function handleFile(event) {
    selectedFile = event.target.files[0];

    if (selectedFile) {
        preview.src = URL.createObjectURL(selectedFile);
        preview.style.display = "block";
    }
}

// ===============================
// MAIN API CALL FUNCTION
// ===============================
async function analyzeImage() {

    if (!selectedFile) {
        alert("Please select or capture an image");
        return;
    }

    document.getElementById("loader").classList.remove("hidden");
    document.getElementById("result").classList.add("hidden");

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {

        const response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        console.log("API RESPONSE:", data); // 🔥 DEBUG

        // ===============================
        // TEXT UI UPDATE
        // ===============================
        document.getElementById("disease").innerHTML = `
            <b>English:</b> ${data.disease_en || "N/A"}<br>
            <b>हिन्दी:</b> ${data.disease_hi || "N/A"}
        `;

        document.getElementById("confidence").innerText =
            (data.confidence ?? 0) + "%";

        document.getElementById("symptoms").innerHTML = `
            <b>English:</b> ${data.symptoms_en || "N/A"}<br><br>
            <b>हिन्दी:</b> ${data.symptoms_hi || "N/A"}
        `;

        document.getElementById("treatment").innerHTML = `
            <b>English:</b> ${data.treatment_en || "N/A"}<br><br>
            <b>हिन्दी:</b> ${data.treatment_hi || "N/A"}
        `;

        document.getElementById("prevention").innerHTML = `
            <b>English:</b> ${data.prevention_en || "N/A"}<br><br>
            <b>हिन्दी:</b> ${data.prevention_hi || "N/A"}
        `;

        document.getElementById("progressBar").style.width =
            (data.confidence ?? 0) + "%";

        // ===============================
        // SPEECH OUTPUT
        // ===============================
        speakResult(data);

        document.getElementById("loader").classList.add("hidden");
        document.getElementById("result").classList.remove("hidden");

    } catch (error) {

        console.error(error);
        alert("Prediction Failed");

        document.getElementById("loader").classList.add("hidden");
    }
}

// ===============================
// VOICE FUNCTION (FIXED)
// ===============================
function speakResult(data) {

    const disease = data.disease_en || "unknown disease";
    const diseaseHi = data.disease_hi || disease;

    const treatment = data.treatment_en || "no treatment available";
    const confidence = data.confidence ?? 0;

    const message =
        `Your plant has ${disease}. 
        Hindi name is ${diseaseHi}. 
        Treatment is ${treatment}. 
        Confidence is ${confidence} percent.`;

    console.log("VOICE MESSAGE:", message);

    // Stop previous speech (important fix)
    window.speechSynthesis.cancel();

    lastSpeech = new SpeechSynthesisUtterance(message);

    lastSpeech.lang = "en-US";  // change to hi-IN if you want Hindi only
    lastSpeech.rate = 0.9;
    lastSpeech.pitch = 1;

    window.speechSynthesis.speak(lastSpeech);
}

// ===============================
// REPLAY VOICE
// ===============================
function speakAgain() {

    if (lastSpeech) {
        window.speechSynthesis.cancel();
        window.speechSynthesis.speak(lastSpeech);
    }
}