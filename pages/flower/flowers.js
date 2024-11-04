document.getElementById('flowerForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const name = document.getElementById('flowerName').value;
    const sci_name = document.getElementById('sciName').value;
    const family = document.getElementById('flowerFamilyName').value;

    const token = localStorage.getItem("token");
    
    // Add Flower using the API
    const res = await fetch('http://localhost:5000/api/flowers', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({ name, sci_name, family })
    });

    if (res.ok) {
        alert('Flower added successfully');
        loadAllFlowers();
    } else {
        alert('Failed to add flower');
    }
})


async function deleteFlower(flowerName) {
    const token = localStorage.getItem("token");

    const res = await fetch(`http://localhost:5000/api/flowers/${flowerName}`, {
        method: 'DELETE',
        headers: {
            "Authorization": `Bearer ${token}`
        }
    });

    if (res.ok) {
        alert("Flower deleted successfully");
        loadAllFlowers();  // Recarrega a lista de flores
    } else {
        alert("Failed to delete flowers");
    }
}


async function loadAllFlowers() {
    const res = await fetch('http://localhost:5000/api/flowers');
    const flowers = await res.json();

    const flowerList = document.getElementById('flowerList');
    flowerList.innerHTML = '';

    flowers.forEach(flower => {
        const div = document.createElement('div');
        const li = document.createElement('li');

        const flowerName = flower.family ? flower.family : 'No family';  // Verifica se a família existe
        li.textContent = `${flower.name} - ${flower.sci_name} - ${flowerName}`;

        const deleteBtn = document.createElement('button')
        deleteBtn.innerText = "Deletar"
        deleteBtn.addEventListener("click", (e) => {
            deleteFlower(flower.id)
        })

        const attBtn = document.createElement('button');
        attBtn.innerText = "Att";
        attBtn.addEventListener("click", (e) => {
            document.location = `attFlower.html?flowerId=${flower.id}`
        }); 

        div.appendChild(li);
        div.appendChild(deleteBtn);
        div.appendChild(attBtn);
        flowerList.appendChild(div);
    });
}



document.addEventListener('DOMContentLoaded', function () {
    loadAllFlowers();
});