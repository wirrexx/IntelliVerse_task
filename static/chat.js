document.addEventListener("DOMContentLoaded", () => {
    console.log("chat.js ready");

    const textarea = document.getElementById("prompt");
    const form = document.getElementById("chat-form");
    const checkbox = document.getElementById("checkDefault");

    if (!textarea || !form) {
        console.error("Textarea or form not found");
        return;
    }

    textarea.addEventListener("keydown", (e) => {
        console.log("Key:", e.key, "Alt:", e.altKey);

        if (checkbox && !checkbox.checked) return;

        if (e.key === "Enter") {
            if (e.altKey) {
                // Alt + Enter → newline
                return;
            }

            // Enter → submit
            e.preventDefault();
            form.requestSubmit(); // safer than form.submit()
        }
    });
});
