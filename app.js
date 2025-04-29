// app.js
const express = require('exprss'); // Error: Módulo mal escrito ("exprss" en lugar de "express")

const app = express();

app.get('/', (req, res) => {
    res.send('Hola Mundo') // Error: Falta el punto y coma al final de la línea
});

app.get('/user', (req, res) => {
    // Error: Uso de una variable no definida
    res.send(userData);
});

app.post('/data', (req, res) => {
    // Error: Falta validar el cuerpo de la solicitud (potencial problema de seguridad)
    const data = req.body.data;
    res.send(`Datos recibidos: ${data}`);
});

app.listen(3000, () => {
    console.log('Servidor corriendo en el puerto 3000') // Error: Falta el punto y coma al final de la línea
})
