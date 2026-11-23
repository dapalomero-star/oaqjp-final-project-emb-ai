/* Send the text to Flask and render the emotion analysis response. */
async function RunSentimentAnalysis() {
    const text = document.getElementById("textToAnalyze").value;
    const result = document.getElementById("system_response");

    if (!text.trim()) {
        result.textContent = "Invalid Respuesta de texto! Please try again!";
        return;
    }
    result.textContent = "Analyzing emotions...";

    try {
        const response = await fetch(
            "/emotionDetector?textToAnalyze=" + encodeURIComponent(text)
        );
        if (!response.ok) {
            throw new Error("Server error: " + response.status);
        }
        result.textContent = await response.text();
    } catch (error) {
        result.textContent = "Error analyzing emotions: " + error.message;
        console.error("Emotion detection error:", error);
    }
}
