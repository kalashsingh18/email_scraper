document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('lost-item-form');
    const itemsList = document.getElementById('items-list');

    form.addEventListener('submit', (event) => {
        event.preventDefault();

        const itemName = document.getElementById('item-name').value;
        const itemDescription = document.getElementById('item-description').value;
        const contactInfo = document.getElementById('contact-info').value;

        const newItem = document.createElement('li');
        newItem.innerHTML = `
            <h3>${itemName}</h3>
            <p>${itemDescription}</p>
            <p><strong>Contact:</strong> ${contactInfo}</p>
        `;

        itemsList.appendChild(newItem);

        form.reset();
    });
});
