function addScriptToHead(id, src, integrity, crossorigin){
    if(!document.getElementById(id)){
        var el = document.createElement("script");
        el.id = id;
        if(src !== undefined){
            el.src = src;}
        if(integrity !== undefined){
            el.integrity = integrity;}
        if(crossorigin !== undefined){
            el.crossorigin = crossorigin;}
        document.head.appendChild(el);}}
function addLinkToHead(id, rel, href, integrity, crossorigin){
    if(!document.getElementById(id)){
        var el = document.createElement("link");
        el.id = id;
        if(rel !== undefined){
            el.rel = rel;}
        if(href !== undefined){
            el.href = href;}
        if(integrity !== undefined){
            el.integrity = integrity;}
        if(crossorigin !== undefined){
            el.crossorigin = crossorigin;}
        document.head.appendChild(el);}}
addLinkToHead("leaflet-css-head", "stylesheet",
    "https://unpkg.com/leaflet@1.5.1/dist/leaflet.css",
);
addScriptToHead("leaflet-js-head", 
    "https://unpkg.com/leaflet@1.5.1/dist/leaflet.js", 
);
addScriptToHead("esri-leaflet-js-head",
    "https://unpkg.com/esri-leaflet/dist/esri-leaflet.js");
if(!document.getElementById("leaflet-providers-head")){
    var el = document.createElement("script");
    el.id = "leaflet-providers-head";
    el.innerHTML = `%{leaflet_providers_js_content}`;}
