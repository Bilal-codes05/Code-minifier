// Sample input file 
function calculateTotal(items) {
    var total = 0;
    for (var i = 0; i < items.length; i++) {
        total += items[i].price * items[i].quantity;
    }
    return total;
}

// Example data
const items = [
    { price: 10, quantity: 2 },
    { price: 5, quantity: 3 }
];

// Call the function and print result
console.log("Total:", calculateTotal(items));
