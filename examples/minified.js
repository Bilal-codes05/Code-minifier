function calculateTotal(a){var b=0;for(var c=0;c<a.length;c++){b+=a[c].price*a[c].quantity;}return b;}

const items=[{price:10,quantity:2},{price:5,quantity:3}];

console.log("Total:",calculateTotal(items));
