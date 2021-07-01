const { response } = require('express');
const fetch = require('node-fetch');
var i = 0;
var fetchNow = function() {
    fetch("http://localhost:8000/sign_up/submit", {
    "headers": {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "sec-ch-ua": "\"Google Chrome\";v=\"89\", \"Chromium\";v=\"89\", \";Not A Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "cookie": "connect.sid=s%3Am8bw4G2liUUI3a0WryAiqkg639wEadXL.4CdI9IxO%2F6D27F%2FQ1tF4Bh9dDJofsTwga10S5rYvgEw"
    },
    "referrer": "https://hcb-app.eu-de.mybluemix.net/sign_up",
    "referrerPolicy": "same-origin",
    "body": "_csrf=03rYXEDR-ya9tN78sDlGmk5d8mGK7mIX8uaI&firstName=Bart&lastName=Script&companyName=IBM&country=Poland&email=tescfee"+i+"%40onet.pl&password=PrzykladoweHaslo%21&confirmed_password=PrzykladoweHaslo%21&ibmemail=yes",
    "method": "POST",
    "mode": "cors"
    }).then(function(res){
    if (res.status==200 & i < 50){
        console.log(res.status)
        i++;
        fetchNow();
    } else {
        console.log(res);
    }
    })
}
fetchNow();