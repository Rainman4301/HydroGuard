// 引入 library
const express = require('express');
// express 引入的是一個 function
const app = express();
// 建立一個不易產生衝突的 port 用來測試
const port = 3000;

const router = express.Router();

const coe = require('./coefficient.json');



app.use('/js', express.static(__dirname + '/js'));
app.use('/css', express.static(__dirname + '/css'));
app.use('/img', express.static(__dirname + '/img'));




app.get('/', function (req, res) {
    res.sendFile(__dirname + "/" + "html" + "/" + "index.html");

    // console.log(coe);

})

app.get('/setting.html', function (req, res) {
    res.sendFile(__dirname + "/" + "html" + "/" + "setting.html");
})

app.get('/system.html', function (req, res) {
    res.sendFile(__dirname + "/" + "html" + "/" + "system.html");
})









app.get('/python', pythonProcess)

function pythonProcess(req, res) {

    // console.log(`name: ${req.query.name}, from: ${req.query.from}`)

    let spawn = require("child_process").spawn

    let process = spawn('python', [
        "./DNN-RI_forecastingSystem/DNN_RI_pred_module.py",
        req.query.factor_1,
        req.query.factor_2,
        req.query.factor_3,
        req.query.factor_4,
        req.query.factor_5,
        req.query.factor_6,
        req.query.factor_7,
        req.query.factor_8,
        req.query.factor_9,        
        req.query.factor_10

    ])

    process.stdout.on('data', (data) => {
        const parsedString = JSON.parse(data)
        res.json(parsedString)
    })

}











// 運行這個 port，參數分別為 port 和要執行的 function
app.listen(port, () => {
    console.log(`Example app listening at http://127.0.1:${port}`)
});