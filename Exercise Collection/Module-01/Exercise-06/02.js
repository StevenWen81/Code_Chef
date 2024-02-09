// Create a program to create transaction

class Product {
    constructor ( name, price ) {
        this.name = name;
        this.price = price;
    }
}

class Transaction {
    constructor() {
        this.products = [];
        this.total = 0;
    }

    addToCart ( product, qty ) {
        this.products.push(
            {product, qty}
        )

        this.total += product.price * qty
    }

    showTotal() {
        console.log(`
            Transaction Total = ${this.total}
        `.trim());
    }

    checkOut() {
        console.log("=====================");
        console.log("Finalized Transaction");
        console.log("=====================");
    
        console.log("Transaction Details:");

        for ( let i of this.products ) {
            console.log(`
                - ${i.product.name} ${i.qty}x ${i.product.price}
            `.trim())
        }
        this.showTotal();
    }
}

const product1 = new Product("Pulpen", 3000);
const product2 = new Product("Buku", 5000);
const product3 = new Product("Penghapus", 2000);

const transaction = new Transaction();

transaction.addToCart(product1, 3);
transaction.addToCart(product2, 2);
transaction.addToCart(product3, 1);

transaction.showTotal();

transaction.checkOut();