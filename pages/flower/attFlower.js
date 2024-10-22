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

    const res = await fetch(`http://localhost:5000/api/flowers/${flowerId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, sciName, familyName})
    });

    if (res.ok) {
        alert("Flor atualizado com sucesso");
        document.location = "flowers.html";
    } else {
        console.error("Update failed:", errorMessage);
        alert("Falha ao atualizar o flor");
    }
});
