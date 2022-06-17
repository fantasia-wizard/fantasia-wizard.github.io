for (i in document.getElementsByTagName("a")) {
    if (document.getElementsByTagName("a")[i].getAttribute("id") == null && document.getElementsByTagName("a")[i].getAttribute("class") == null) {
        document.getElementsByTagName("a")[i].setAttribute("class", "hyperlink")
        document.getElementsByTagName("a")[i].innerHTML = document.getElementsByTagName("a")[i].innerHTML.replace(/(^https:\/\/)/gi, "")
    }
}