document.getElementById('purchaseForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const price = parseInt(document.getElementById('purchasePrice').value);
    const payment_method = document.getElementById('purchaseMethod').value;
    const client_name = document.getElementById('purchaseClient').value;
    const flower_name = document.getElementById('purchaseFlower').value;

    const token = localStorage.getItem("token");

    const res = await fetch('http://localhost:5000/api/purchases', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({ payment_method, price, client_name, flower_name })
    });

    const result = await res.json();

    if (res.ok) {
        alert('Purchase added successfully');
        loadAllPurchases();
    } else {
        alert(`Failed to add purchase: ${result.message}`);
    }
});

async function loadAllPurchases() {
    const res = await fetch('http://localhost:5000/api/purchases');
    const purchases = await res.json();

    const purchaseList = document.getElementById('purchaseList');
    purchaseList.innerHTML = '';

    purchases.forEach(purchase => {
        const div = document.createElement('div');
        const li = document.createElement('li');

        li.textContent = `${purchase.price}$ ${purchase.payment_method} - ${purchase.flower} - ${purchase.client}`;

        const btn = document.createElement('button')
        btn.addEventListener("click", (e) => {
            deleteFlower(purchase.id)
        })

        div.appendChild(li);
        div.appendChild(btn);

        purchaseList.appendChild(div);
    });
}

async function deletePurchase(purchaseName) {
    const token = localStorage.getItem("token");

    const res = await fetch(`http://localhost:5000/api/purchases/${purchaseName}`, {
        method: 'DELETE',
        headers: {
            "Authorization": `Bearer ${token}`
        }
    });

    if (res.ok) {
        alert("Purchase deleted successfully");
        loadAllPurchases();  // Recarrega a lista de compras
    } else {
        alert("Failed to delete purchases");
    }
}

document.addEventListener('DOMContentLoaded', function () {
    loadAllPurchases();
});
