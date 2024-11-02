document.getElementById('clientForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const name = document.getElementById('clientName').value;
    const email = document.getElementById('clientEmail').value;

    // Add Client using the API
    const token = localStorage.getItem("token"); 

    const res = await fetch("http://localhost:5000/api/clients", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({ name, email })
    });

    if (res.ok) {
        alert('Cliente adicionado com sucesso');
        loadAllClients();
    } else {
        alert('Falha ao adicionar o cliente');
    }
});


async function deleteClient(clientId) {
    const token = localStorage.getItem("token");

    const res = await fetch(`http://localhost:5000/api/clients/${clientId}`, {
        method: 'DELETE',
        headers: {
            "Authorization": `Bearer ${token}`
        }
    });

    if (res.ok) {
        alert("Cliente deletado com sucesso");
        loadAllClients();
    } else {
        alert("Falha ao deletar cliente");
    }
}

async function loadAllClients() {
    const res = await fetch('http://localhost:5000/api/clients');
    const clients = await res.json();

    const clientList = document.getElementById('clientList');
    clientList.innerHTML = '';
    
    clients.forEach(client => {
        const div = document.createElement('div');

        const li = document.createElement('li');
        li.textContent = `${client.name} (${client.email})`;

        const deleteBtn = document.createElement('button');
        deleteBtn.innerText = "Delete";
        deleteBtn.addEventListener("click", (e) => {
            deleteClient(client.id)
        });

        const attBtn = document.createElement('button');
        attBtn.innerText = "Att";
        attBtn.addEventListener("click", (e) => {
            document.location = `attClient.html?clientId=${client.id}`
        }); 

        div.appendChild(li);
        div.appendChild(deleteBtn);
        div.appendChild(attBtn);
        clientList.appendChild(div)
    });
}

document.addEventListener('DOMContentLoaded', function () {
    loadAllClients();
});