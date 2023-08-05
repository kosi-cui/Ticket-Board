window.onload = async function SetUpTable()
{   
    await TableCreation();
    delay(1000).then(() => ShowReimages());
}

function ShowReimages()
{
    document.querySelector("#loader").style.visibility = "hidden";
    document.querySelector("#ReimageTable").style.visibility = "visible";
    document.querySelector("#TicketButton").style.visibility = "visible";
}

function HideReimages()
{
    document.querySelector("#loader").style.visibility = "visible";
    document.querySelector("#ReimageTable").style.visibility = "hidden";
    document.querySelector("#TicketButton").style.visibility = "hidden";
}

//#region Async window load functions
async function TableCreation()
{
    files = await GetTicketFiles();
    await CreateRows(files);
    return;
}

async function GetTicketFiles()
{
    eel.Eel_Print("Getting the ticket files");
    ticketFiles = await eel.Eel_ExposeTickets()();
    eel.Eel_Print("Got the ticket files");
    return ticketFiles;
}

async function GetTicketJSON(ticketFile)
{
    fetch(ticketFile)
        .then(response => response.json())
        .then(json => {
            eel.Eel_Print("Got the JSON for " + ticketFile);
            addTableRow(json["web_data"]);
        });
    return;
}

async function CreateRows(file_list)
{
    file_list.forEach(element => {
        GetTicketJSON(element);
    });
    return;
}

function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
//#endregion


function addTableRow(rowData)
{
    var table = document.getElementById("ReimageTable");
    var rowCount = table.rows.length;
    var row = table.insertRow(rowCount);

    // Cell 0 is the checkbox -- Creating the checkbox
    var tBox = document.createElement("input");
    tBox.setAttribute("type", "checkbox");
    tBox.setAttribute("value", "completed");
    tBox.setAttribute("id", "select_" + rowData["name"]);

    // Cell 2 is the drop-down -- Creating the drop-down
    var dropDown = document.createElement("select");
    rowData["steps"].forEach(element => {
        var option = document.createElement("option");
        option.text = element;
        option.value = element;
        dropDown.appendChild(option);
    });


    row.insertCell(0).innerHTML = tBox.outerHTML;
    row.insertCell(1).innerHTML = rowData["name"];
    row.insertCell(2).innerHTML = dropDown.outerHTML;
    row.insertCell(3).innerHTML = rowData["creation_date"];
    row.insertCell(4).innerHTML = rowData["assigned_to"];
}

document.onreadystatechange = function () {
    if(document.readyState !== "complete")
    {
      eel.Eel_Print("Loading the page");  
    }
    else
    {
        eel.Eel_Print("Page loaded");
    }
};