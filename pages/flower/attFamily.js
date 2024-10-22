document.getElementById('attFamilyForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const familyName = document.getElementById('familyName').value;

    const urlParams = new URLSearchParams(window.location.search);
    const familyId = urlParams.get('familyId');

    if (!familyId) {
        alert("Flower ID is missing!");
        return;
    }

    const res = await fetch(`http://localhost:5000/api/families/${familyId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ familyName })
    });

    if (res.ok) {
        alert("Familia atualizado com sucesso");
        document.location = "flowers.html";
    } else {
        console.error("Update failed:", errorMessage);
        alert("Falha ao atualizar o familia");
    }
});
