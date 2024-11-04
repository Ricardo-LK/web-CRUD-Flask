document.getElementById('attFlowerForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const name = document.getElementById('flowerName').value;
    const sciName = document.getElementById('sciName').value;
    const familyName = document.getElementById('flowerFamilyName').value;


    const urlParams = new URLSearchParams(window.location.search);
    const flowerId = urlParams.get('flowerId');

    if (!flowerId) {
        alert("Flower ID is missing!");
        return;
    }

    const token = localStorage.getItem("token");

    const res = await fetch(`http://localhost:5000/api/flowers/${flowerId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({ name, sciName, familyName})
    });

    if (res.ok) {
        document.location = "./flowers.html";
        alert("Flor atualizado com sucesso");
    } else {
        alert("Falha ao atualizar o flor");
    }
});
