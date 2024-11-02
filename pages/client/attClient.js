document.getElementById('attClientForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const name = document.getElementById('clientName').value;
    const email = document.getElementById('clientEmail').value;

    const urlParams = new URLSearchParams(window.location.search);
    const clientId = urlParams.get('clientId');

    if (!clientId) {
        alert("Client ID is missing!");
        return;
    }

    const token = localStorage.getItem("token");

    const res = await fetch(`http://localhost:5000/api/clients/${clientId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({ name, email })
    });

    if (res.ok) {
        alert("Cliente atualizado com sucesso");
        document.location = "clients.html";
    } else {
        alert("Falha ao atualizar o cliente");
    }
});