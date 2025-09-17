const express = require("express");
const cors = require("cors");
const app = express();
const port = process.env.PORT || 5000;

app.use(cors()); // ✅ allow frontend requests

app.get("/api/hello", (req, res) => {
  res.json({ service: "microservice1", message: "Hello from Microservice 1!" });
});

app.listen(port, () => {
  console.log(`Microservice1 running on port ${port}`);
});

