import { Order } from "../models/Order";

export class OrderService {

    private orders: Order[] = [];

    createOrder(product: string, quantity: number, price: number): Order {

        const newOrder = new Order(
            this.orders.length + 1,
            product,
            quantity,
            price,
            "CREATED"
        );

        this.orders.push(newOrder);

        return newOrder;
    }

    getOrders(): Order[] {
        return this.orders;
    }

    approveOrder(id: number): Order | undefined {

        const order = this.orders.find(o => o.id === id);

        if(order){
            order.status = "APPROVED";
        }

        return order;
    }

}