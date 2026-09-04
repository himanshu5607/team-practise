async function analyzeEmail() {

    const email = document.getElementById("email").value;

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/analyze",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    email: email
                })
            }
        );

        if (!response.ok) {
            throw new Error("Backend returned an error");
        }

        const data = await response.json();

        document.getElementById("classification").innerText =
            "Classification: " + data.classification;

        document.getElementById("risk").innerText =
            "Risk Score: " + data.risk_score;

        document.getElementById("reason").innerText =
            "Reason: " + data.reason;

    } catch (error) {

        console.error(error);

        document.getElementById("classification").innerText =
            "Error connecting to backend";

    }
}