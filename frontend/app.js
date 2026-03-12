const API = "http://localhost:3000/api";

async function createOrder(){

const product = document.getElementById("product").value;
const quantity = document.getElementById("quantity").value;
const price = document.getElementById("price").value;

await fetch(API + "/order",{

method:"POST",
headers:{
"Content-Type":"application/json"
},
body: JSON.stringify({
product,
quantity,
price
})

});

loadOrders();

}

async function loadOrders(){

const res = await fetch(API + "/orders");

const orders = await res.json();

const list = document.getElementById("orders");

list.innerHTML = "";

orders.forEach(o => {

const li = document.createElement("li");

li.innerHTML = `Pedido ${o.id} - ${o.product} - ${o.status}`;

list.appendChild(li);

});

}

loadOrders();