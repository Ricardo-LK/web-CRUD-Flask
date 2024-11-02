document.getElementById('familyForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const name = document.getElementById('familyName').value;
    
    const token = localStorage.getItem("token");
    
    // Add Family using the API
    const res = await fetch('http://localhost:5000/api/families', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({ name })
    });

    if (res.ok) {
        alert('Family added successfully');
        loadAllClients();
    } else {
        alert('Failed to add family');
    }
})

async function loadAllFamilies() {
    const res = await fetch('http://localhost:5000/api/families');
    const families = await res.json();

    const familyList = document.getElementById('familyList');
    familyList.innerHTML = '';

    families.forEach(family => {
        const div = document.createElement('div');
        const li = document.createElement('li');
        li.textContent = `${family.name}`;

        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = "Delete";
        deleteBtn.addEventListener("click", () => {
            deleteFamily(family.name);
        });

        const dattBtn = document.createElement('button');
        dattBtn.innerText = "Att";
        dattBtn.addEventListener("click", (e) => {
            document.location = `attFamily.html?familyId=${family.id}`
        }); 

        div.appendChild(li);
        div.appendChild(deleteBtn);
        div.appendChild(dattBtn);
        familyList.appendChild(div);
    });
}

// Função para deletar uma família
async function deleteFamily(familyName) {
    const token = localStorage.getItem("token");

    const res = await fetch(`http://localhost:5000/api/families/${familyName}`, {
        method: 'DELETE',
        headers: {
            "Authorization": `Bearer ${token}`
        }
    });

    if (res.ok) {
        alert("Family deleted successfully");
        loadAllFamilies();  // Recarrega a lista de famílias
    } else {
        alert("Failed to delete family");
    }
}

document.addEventListener('DOMContentLoaded', function () {
    loadAllFamilies();
});