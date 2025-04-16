const apiBase = "/items"; // FastAPI router is mounted at /items

async function fetchItems() {
  const res = await fetch(apiBase + "/");
  if (!res.ok) throw new Error("Failed to fetch items");
  return await res.json();
}

async function addItem(name, description) {
  const res = await fetch(apiBase + "/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, description }),
  });
  if (!res.ok) throw new Error("Failed to add item");
  return await res.json();
}

async function deleteItem(id) {
  const res = await fetch(`${apiBase}/${id}`, { method: "DELETE" });
  if (!res.ok) throw new Error("Failed to delete item");
}

function renderItems(items) {
  const list = document.getElementById("itemList");
  list.innerHTML = "";
  items.forEach((item) => {
    const li = document.createElement("li");
    li.innerHTML = `
            <strong>${item.name}</strong>: ${item.description}
            <button data-id="${item._id}" class="delete-btn">Delete</button>
        `;
    list.appendChild(li);
  });
  document.getElementById("itemCount").textContent =
    `Total items: ${items.length}`;
}

let allItems = [];

async function loadAndRenderItems(search = "") {
  allItems = await fetchItems();
  let itemsToShow = allItems;
  if (search.trim()) {
    const s = search.toLowerCase();
    itemsToShow = allItems.filter(
      (item) =>
        item.name.toLowerCase().includes(s) ||
        item.description.toLowerCase().includes(s),
    );
  }
  renderItems(itemsToShow);
}

document.addEventListener("DOMContentLoaded", () => {
  loadAndRenderItems();

  document.getElementById("itemForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const name = document.getElementById("name").value.trim();
    const description = document.getElementById("description").value.trim();
    if (!name || !description) return;
    await addItem(name, description);
    document.getElementById("itemForm").reset();
    loadAndRenderItems(document.getElementById("search").value);
  });

  document.getElementById("search").addEventListener("input", (e) => {
    loadAndRenderItems(e.target.value);
  });

  document.getElementById("itemList").addEventListener("click", async (e) => {
    if (e.target.classList.contains("delete-btn")) {
      const id = e.target.getAttribute("data-id");
      await deleteItem(id);
      loadAndRenderItems(document.getElementById("search").value);
    }
  });
});
