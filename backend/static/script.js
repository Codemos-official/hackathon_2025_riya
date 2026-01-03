function addApplication() {
    const nameInput = document.getElementById("name");
    const companyInput = document.getElementById("company");
    const list = document.getElementById("list");

    const name = nameInput.value.trim();
    const company = companyInput.value.trim();

    if (!name || !company) {
        alert("Please enter both Name and Company!");
        return;
    }

    const li = document.createElement("li");
    li.innerHTML = `<span>${name} - ${company}</span> <button onclick="removeApplication(this)">Delete</button>`;

    list.appendChild(li);

    nameInput.value = "";
    companyInput.value = "";
}

function removeApplication(button) {
    button.parentElement.remove();
}
