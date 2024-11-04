document.getElementById("registerForm").onsubmit = async (e) => {
    e.preventDefault();

    const name = document.getElementById("name").value;
    const pass = document.getElementById("password").value;

    const res = await fetch("http://localhost:5000/api/register", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name, pass })
    });

    const data = await res.json();
    document.location = "../../index.html";
    alert(data.message);
}