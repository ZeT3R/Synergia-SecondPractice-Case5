async function addTrip() {
    const data = {
        user_id: document.getElementById('user_id').value,
        location: document.getElementById('loc').value,
        img: document.getElementById('img').value,
        cost: document.getElementById('cost').value,
        desc: "..."
    };
    await fetch('/trips/', { method: 'POST', body: JSON.stringify(data) });
    loadTrips();
}

async function loadTrips() {
    const res = await fetch('/trips/');
    const trips = await res.json();
    document.getElementById('trips-list').innerHTML = trips.map(t => `<div>${t.location} - $${t.cost}</div>`).join('');
}
