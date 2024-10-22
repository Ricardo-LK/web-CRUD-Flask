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

    const res = await fetch(`http://localhost:5000/api/clients/${clientId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, email })
    });

    if (res.ok) {
        alert("Cliente atualizado com sucesso");
        document.location = "clients.html";
    } else {
        console.error("Update failed:", errorMessage);
        alert("Falha ao atualizar o cliente");
    }
});
