
// 顯示時間
function ShowTime() {
    var NowDate = new Date();
    var h = NowDate.getHours();
    var m = NowDate.getMinutes();
    var s = NowDate.getSeconds();
    document.getElementById('showbox').innerHTML = '現在時間:' + h + '時' + m + '分' + s + '秒';
    setTimeout('ShowTime()', 1000);
}



//位置顯示
function place(choice) {

    // console.log(choice.value);

    t = document.querySelector("#ti_co");
    switch (choice.value) {
        case "1":

            t.innerHTML = "現在位置:Taipei city";
            break;

        case "2":

            t.innerHTML = "現在位置:Taoyuan city";
            break;
        case "3":

            t.innerHTML = "現在位置:Taichung city";
            break;
        case "4":

            t.innerHTML = "現在位置:Alishan";
            break;
        case "":
            t.innerHTML = "現在位置:";
            break;

        default:
    }

}


// //網頁跳轉
// function home() {
//     window.location.href = 'c:/Users/user/OneDrive/桌面/決賽程式/HydroGaurd/html/index.html';

// }

// function system() {
//     window.location.href = 'c:/Users/user/OneDrive/桌面/決賽程式/HydroGaurd/html/system.html';
// }

// function setting() {
//     window.location.href = 'c:/Users/user/OneDrive/桌面/決賽程式/HydroGaurd/html/setting.html';
// }


//未來時間
function time(option) {

    let t = document.querySelector(".result2");
    let r = document.querySelector(".result3");

    switch (option.value) {
        case ("6"):
            t.innerHTML = "未來6小時預報結果:";
            r.innerHTML = " <h1>因子列表</h1>測站氣壓(hPa): 35<br>海平面氣壓(hPa): 35<br>氣溫(c): 45<br>露點溫度(c): 45<br>相對溼度(%): 35<br>水氣壓(hPa): 60<br>平均風風速(m/s): 80<br>平均風風向(360˙): 40<br>降水量(mm): 40<br>降水時數(hr): 60"
            break;

        case ("12"):
            t.innerHTML = "未來12小時預報結果:";
            r.innerHTML = " <h1>因子列表</h1>測站氣壓(hPa): 35<br>海平面氣壓(hPa): 35<br>氣溫(c): 45<br>露點溫度(c): 45<br>相對溼度(%): 35<br>水氣壓(hPa): 60<br>平均風風速(m/s): 80<br>平均風風向(360˙): 40<br>降水量(mm): 40<br>降水時數(hr): 60"
            break;

        case ("18"):
            t.innerHTML = "未來18小時預報結果:";
            r.innerHTML = " <h1>因子列表</h1>測站氣壓(hPa): 35<br>海平面氣壓(hPa): 35<br>氣溫(c): 45<br>露點溫度(c): 45<br>相對溼度(%): 35<br>水氣壓(hPa): 60<br>平均風風速(m/s): 80<br>平均風風向(360˙): 40<br>降水量(mm): 40<br>降水時數(hr): 60"
            break;

        case ("24"):
            t.innerHTML = "未來24小時預報結果:";
            r.innerHTML = " <h1>因子列表</h1>測站氣壓(hPa): 35<br>海平面氣壓(hPa): 35<br>氣溫(c): 45<br>露點溫度(c): 45<br>相對溼度(%): 35<br>水氣壓(hPa): 60<br>平均風風速(m/s): 80<br>平均風風向(360˙): 40<br>降水量(mm): 40<br>降水時數(hr): 60"
            break;

        case (""):
            t.innerHTML = "未來_預報結果:";
            r.innerHTML = ""
            break;


        default:

    }




};






/*

const http = require("http");
const fs = require("fs");
const qs = require("querystring");



// var app = express();


const port = 3000;
const ip = "127.0.0.1";




const sendResponse = (filename, statusCode, response) => {
    fs.readFile(`./html/${filename}`, (error, data) => {
        if (error) {
            response.statusCode = 500;
            response.setHeader("Content-Type", "text/plain");
            response.end("Sorry, internal error");
        }
        else {
            response.statusCode = statusCode;
            response.setHeader("Content-Type", "text/html");
            response.end(data);
        }
    });
};









const server = http.createServer((request, response) => {
    console.log(request.url, request.method);

    const method = request.method;
    const url = request.url;



    if (method === "GET") {
        if (url === "/") {
            sendResponse("index.html", 200, response);
        }
        else if (url === "/system.html") {
            sendResponse("system.html", 200, response);
        }
        else if (url === "/setting.html") {
            sendResponse("setting.html", 200, response);
        }
        else {
            sendResponse("404.html", 404, response);
        }
    }

    else {

    }
});







server.listen(port, ip, () => {
    console.log(`Server is running at http://${ip}:${port}`);
});




*/





