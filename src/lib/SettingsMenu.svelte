<script>
import { invoke } from "@tauri-apps/api";
import { createEventDispatcher } from "svelte";

const dispatch = createEventDispatcher();

export let credentials = {};

$ : credentials && updateCredentials(); 

let apiKey = "";
let domain = "";


function updateCredentials() {
    apiKey = credentials[0];
    domain = credentials[1];
}

function emitChanges() {
    dispatch("credentials", {
        key: apiKey,
        domain: domain,
    });
    credentials = [apiKey, domain];
}

const apiUpdate = (event) => {
    apiKey = event.target.value;
}

const domainUpdate = (event) => {
    domain = event.target.value;
}

</script>


<div id="settingsMenu">
    <div id="settingsMenuTitle">
        <h1>Settings</h1>
    </div>
    <div id="line"></div>
    <div id="apiInput">
        <h2>API Key</h2>
        <input type="text" id="apiInputBox" placeholder="API Key" value={apiKey} on:input = {apiUpdate}>
    </div>
    <div id="domainInput">
        <h2>Domain</h2>
        <input type="text" id="domainInputBox" placeholder="Domain" value={domain} on:input = {domainUpdate}>
    </div>
    <div id="settingsMenuButtons">
        <button type="button" id="saveButton" on:click={emitChanges}>Save</button>
    </div> 
</div>


<style>
#settingsMenu {
    position: absolute;
    top: 6.8%;
    right: 32%;
    width: 30%;
    height: 36%;
    z-index: 100;
    transition: 0.5s;
    transform: translateX(100%);
    border: 3px solid #ccd0d4;
    border-radius: 10px 10px 10px 10px;
    text-align: center;
    font-family: Arial, Helvetica, sans-serif;
    background-color: #004c23;
    color: white;
}

#settingsMenu input {
    width: 50%;
    border: none;
    border-radius: 5px 5px 5px 5px;
    font-size: 18px;
    text-align: center;
}

#line {
    position: absolute;
    top: 18%;
    left: 5%;
    width: 90%;
    height: 2px;
    background-color: #ccd0d4;
}

#settingsMenuButtons {
    position: absolute;
    bottom: 2%;
    left: 5%;
    width: 90%;
    height: 20%;
}

#settingsMenuButtons button {
    width: 40%;
    height: 70%;
    border: none;
    border-radius: 10px 10px 10px 10px;
    font-size: 18px;
    box-shadow: 0 7px #999;
}

#settingsMenuButtons button:active {
    background-color: #ccd0d4;
    box-shadow: 0 4px #666;
    transform: translateY(4px);
}

#settingsMenuButtons button:hover {
    background-color: #ccd0d4;
}
</style>