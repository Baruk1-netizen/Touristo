// Initialize and display the map
var map = L.map('map').setView([-1.4024, 36.7699], 12); // Nairobi National Park coordinates

// Add OpenStreetMap tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Marker for Nairobi National Park
L.marker([-1.4024, 36.7699]).addTo(map)
    .bindPopup('Nairobi National Park')
    .openPopup();

// Marker for hotels near Nairobi National Park
L.marker([-1.3937, 36.9014]).addTo(map)
    .bindPopup('Panari Hotel');

L.marker([-1.3209, 36.8070]).addTo(map)
    .bindPopup('Eka Hotel');

L.marker([-1.3241, 36.8802]).addTo(map)
    .bindPopup('Decasa Hotel');

L.marker([-1.3035, 36.8489]).addTo(map)
    .bindPopup('The Boma Nairobi');

L.marker([-1.3154, 36.8352]).addTo(map)
    .bindPopup('Ole Sereni Hotel');

L.marker([-1.3106, 36.8273]).addTo(map)
    .bindPopup('Radisson Blu Hotel');

// Marker for city malls near Nairobi National Park
L.marker([-1.2056, 36.8905]).addTo(map)
    .bindPopup('Garden City Mall');

L.marker([-1.3203, 36.7571]).addTo(map)
    .bindPopup('Galleria Mall');

L.marker([-1.3556, 36.7079]).addTo(map)
    .bindPopup('NextGen Mall');

L.marker([-1.3557, 36.6908]).addTo(map)
    .bindPopup('South Field Mall');

L.marker([-1.3284, 36.8446]).addTo(map)
    .bindPopup('Dynamic Mall');

L.marker([-1.3199, 36.8679]).addTo(map)
    .bindPopup('Gateway Mall');
