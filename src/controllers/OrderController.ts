import express from "express";
import { OrderService } from "../services/OrderService";

const router = express.Router();
const service = new OrderService();

router.post("/order", (req, res) => {

    const {product, quantity, price} = req.body;

    const order = service.createOrder(product, quantity, price);

    res.json(order);

});

router.get("/orders", (req, res) => {

    res.json(service.getOrders());

});

router.post("/approve/:id", (req, res) => {

    const id = parseInt(req.params.id);

    const order = service.approveOrder(id);

    res.json(order);

});

export default router;