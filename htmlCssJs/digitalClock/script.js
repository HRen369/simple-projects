const months = ["January","Febuary","March","April","May","June","July","August","September","October","November","December"];
const days = ["Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];

function digitalMinutesSeconds(date){
    timeStr = "";
    if(date.getMinutes() < 10){
        timeStr += "0";
    }
    timeStr += date.getMinutes() + ":";

    if(date.getSeconds() < 10){
        timeStr += "0";
    }
    return ":" + timeStr + date.getSeconds();
}

function digitalDate(date){
    let dateStr = days[date.getDay()] + ", " + months[date.getMonth()] + " " +  date.getDate()
    let dateNumber = date.getDate();

    while(dateNumber > 10){
        dateNumber -= 10
    }

    if(dateNumber == 1){
        dateStr += "st";
    } else if(dateNumber == 2){
        dateStr += "nd";
    }else if(dateNumber == 3){
        dateStr += "rd";
    }
    else{
        dateStr += "th";
    }

    return dateStr + " " + date.getFullYear();
}

// Regular Time
function regularTime(today){
    let timeStr = digitalMinutesSeconds(today);
    let currentHours = today.getHours();
    let isAm = undefined;

    if(currentHours > 12){
        currentHours -= 12;
        isAm = false;
    }
    else{
        isAm = true;
    }

    timeStr = currentHours + timeStr;
    if(currentHours < 10){
        timeStr = "0" + timeStr + " ";
    }
    
    if(isAm){
        return timeStr + "AM";
    }
    return timeStr + "PM";
}

function regularHandleDateTime(){
    let today = new Date();
    let timeStr = regularTime(today);
    let dateStr = digitalDate(today);

    document.getElementById("time").innerHTML = timeStr;
    document.getElementById("date").innerHTML = dateStr;
}

//Military Time
function militaryTime(today){
    let timeStr = digitalMinutesSeconds(today);
    let currentHours = today.getHours();

    if(currentHours < 10){
        timeStr += "0";
    }

    return currentHours + timeStr;
}

function militaryHandleDateTime(){
    let today = new Date();
    let timeStr = militaryTime(today);
    let dateStr = digitalDate(today);

    document.getElementById("time").innerHTML = timeStr;
    document.getElementById("date").innerHTML = dateStr;
}

regularHandleDateTime();
let intervalFunc = setInterval(regularHandleDateTime,1000);

function switchToMilitary(){
    clearInterval(intervalFunc);
    intervalFunc = setInterval(militaryHandleDateTime, 1000);
    militaryHandleDateTime();
    document.getElementById("switch-format").removeAttribute('onclick');
    document.getElementById("switch-format").setAttribute('onclick', "switchToRegular()");
    document.getElementById("switch-format").innerHTML = "Switch to Regular Time";
}


function switchToRegular(){
    clearInterval(intervalFunc);
    intervalFunc = setInterval(regularHandleDateTime,1000);
    regularHandleDateTime();
    document.getElementById("switch-format").removeAttribute('onclick');
    document.getElementById("switch-format").setAttribute('onclick', "switchToMilitary()");
    document.getElementById("switch-format").innerHTML = "Switch to Military Time";
}