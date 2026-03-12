export class Order {

    constructor(
        public id: number,
        public product: string,
        public quantity: number,
        public price: number,
        public status: string
    ){}

}