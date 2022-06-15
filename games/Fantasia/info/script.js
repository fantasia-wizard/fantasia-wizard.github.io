var versions = ["1", "1.5", "1.5.1", "1.6", "1.6.5", "1.6.6"];
var contents = ["Changelog", "License"]
var sections = ["Fantasia", "Plugins", "Engine", "Fonts"]

for (i in versions){
    var menu = document.getElementById("version-menu-content");
    var new_item = document.createElement("a");
    menu.appendChild(new_item);
    new_item.href = "#" + versions[i];
    new_item.innerHTML = versions[i];
}
for (i in contents){
    var content_name = '';
    switch (contents[i]){
        case 'Changelog':
            content_name = 'Changelog';
            break;
        case 'License':
            content_name = 'License and Legal Info'
            break;
    }
    if (content_name == ''){
        content_name = contents[i]
    }
    var menu = document.getElementById("contents-menu-content");
    var new_item = document.createElement("a");
    menu.appendChild(new_item);
    new_item.href = "#" + contents[i];
    new_item.innerHTML = content_name;
}
for (i in sections){
    var menu = document.getElementById("legal-menu-content");
    var new_item = document.createElement("a");
    menu.appendChild(new_item);
    new_item.href = "#" + sections[i];
    new_item.innerHTML = sections[i];
}
