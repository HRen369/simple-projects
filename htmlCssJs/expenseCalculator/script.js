let id = 0;

function removeItem(i){
    let table = document.getElementById('expense-table')
    let pickeditem = document.getElementById(i);
    table.removeChild(pickeditem);
}

function submitItem(){
    let removeItem = `onclick="removeItem(${id})"`;

    let paymentName = document.getElementById("payment-name");
    let paymentType = document.getElementById("payment-type");
    let paymentDate = document.getElementById("payment-date");
    let paymentAmount = document.getElementById("payment-amount");

    const node = document.createElement("tr");
    
    let textNodeStr = `<td>${paymentType.value}</td>`;
    textNodeStr += `<td>${paymentName.value}</td>`;
    textNodeStr += `<td>${paymentDate.value}</td>`;
    textNodeStr += `<td>${paymentAmount.value}</td>`;
    textNodeStr += `<td ${removeItem}>X</td>`;
    
    node.setAttribute('id',`${id}`)
    node.innerHTML = textNodeStr;
 
    document.getElementById('expense-table').appendChild(node);

    id += 1;

}