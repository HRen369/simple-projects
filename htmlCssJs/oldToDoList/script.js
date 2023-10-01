let id = 0;

function deleteTask(i){
    let tasks = document.getElementById("to-dos");
    let pickedTask = document.getElementById(i)
    tasks.removeChild(pickedTask);
}

function addToDo(taskString){
    let functStr = `onclick="deleteTask(${id})"`;
    let addCheckStr = `onclick="addCheck(${id})"`;

    let toDoStr = `<div id="${id}" class="to-do">`;
    toDoStr += `<div class="check-box-unchecked" ${addCheckStr}></div>`;
    toDoStr += taskString;
    toDoStr += `<div class="delete-box" ${functStr}>x</div>`;
    return toDoStr + `</div>`;

}

function addCheck(i){
    let pickedTask = document.getElementById(i);
    pickedTask.firstChild.removeAttribute('class');
    pickedTask.firstChild.setAttribute('class','check-box-checked')

    pickedTask.firstChild.removeAttribute('onclick');
    pickedTask.firstChild.setAttribute('onclick', `removeCheck(${i})`);
}

function removeCheck(i){
    let pickedTask = document.getElementById(i)
    pickedTask.firstChild.removeAttribute('class');
    pickedTask.firstChild.setAttribute('class','check-box-unchecked')

    
    pickedTask.firstChild.removeAttribute('onclick');
    pickedTask.firstChild.setAttribute('onclick', `addCheck(${i})`);
}

document.getElementById("add-to-do").addEventListener('keypress', function(event){
    if(event.key === "Enter"){
        document.getElementById('to-dos').innerHTML += addToDo(event.target.value);
        event.target.value = "";
        id += 1;
    }
})