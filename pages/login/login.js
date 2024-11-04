document.getElementById("loginForm").onsubmit = async (e) => {
    e.preventDefault();
    const name = document.getElementById("name").value;
    const pass = document.getElementById("password").value;

    const res = await fetch("http://localhost:5000/api/login", {
        method: "POST",
        headers: {      
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name, pass })
    });

    const data = await res.json();
    if (res.ok) {
        localStorage.setItem("token", data.token);
        document.location = "../../index.html";
        alert("Login bem-sucedido!");
    } else {
        alert(data.message);
    }
};