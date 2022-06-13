var games = ["platformer", "steve", "Fantasia"];
for (var i in games){
  const app = document.createElement("div");
  const new_app = document.createElement("a");
  const new_app_image = document.createElement("img");
  const new_app_title = document.createElement("p");
  document.getElementById("cat").appendChild(app);
  app.appendChild(new_app);
  app.setAttribute("class", "app");
  new_app.href = "../games/" + games[i];
  new_app.appendChild(new_app_image);
  new_app_image.src = "../games/" + games[i] + "/media/icon.png";
  new_app_image.style.width = "100%";
  new_app_image.alt = "Icon for " + games[i];
  new_app_image.setAttribute("class", "app-image")
  new_app.appendChild(new_app_title);
  new_app_title.innerHTML = games[i];
}
