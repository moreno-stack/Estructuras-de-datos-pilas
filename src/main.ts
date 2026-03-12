import express from "express";
import cors from "cors";
import orderController from "./controllers/OrderController"; // O como lo tengas abajo

const app = express();
const PORT = 3000;

app.listen(PORT, () => {
    console.log(`Servidor corriendo en http://localhost:${PORT}`);
});

app.use(cors());
app.use(express.json());

app.use("/api", orderController);

app.listen(3000, () => {
    console.log("Servidor corriendo en puerto 3000");
});