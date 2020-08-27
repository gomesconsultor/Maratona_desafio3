const express = require('express')
const {
    dir
} = require('console')
const app = express()
const port = 3000

app.get('/', (req, res) => {
    res.send('Eu sou Full Cycle')
})

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
})