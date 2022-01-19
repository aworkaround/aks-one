// Getting the Data
let getEntries = () => {
  $.ajax({
    headers: { Accept: "application/json" },
    type: "GET",
    url: "http://192.168.10.10:8080/api/entry",
    crossDomain: true,
    success: function (data, textStatus, request) {
      let tableBody = document.getElementById("tbody");
      let dt = "";
      data = data["Message"];
      Entries = data["Message"];
      for (let i = 0; i < data.length; i++) {
        dt +=
          "<tr><td>" +
          data[i]["username"] +
          "</td><td>" +
          data[i]["email"] +
          "</td><td>" +
          data[i]["year_of_birth"] +
          "</td><td>" +
          data[i]["age_group"] +
          "</td></tr>";
      }
      tableBody.innerHTML = dt;
    },
  });
};

let randomEntry = () => {
  $.ajax({
    headers: { Accept: "application/json" },
    type: "GET",
    url: "http://192.168.10.10:8081/random-entry",
    crossDomain: true,
    success: function (data, textStatus, request) {
      let username = document.getElementById("username");
      let email = document.getElementById("email");
      let birthyear = document.getElementById("birthyear");
      username.value = data['Message']['username']
      email.value = data['Message']['email']
      birthyear.value = data['Message']['year_of_birth']
    },
  });
};

function send(btn) {
  let username = document.getElementById("username").value;
  let email = document.getElementById("email").value;
  let birthyear = document.getElementById("birthyear").value;
  let Entries = null;
  var person = {
    username: username,
    email: email,
    birthyear: birthyear,
  };
  Entries += person;
  btn.innerHTML = "sending..";
  btn.className = "btn btn-success disabled";

  var xmlhttp = new XMLHttpRequest();
  xmlhttp.open("POST", "http://192.168.10.10:8080/api/entry");
  xmlhttp.setRequestHeader("Content-Type", "application/json");
  xmlhttp.send(JSON.stringify(person));
  location.reload();

  username.value = "";
  email.value = "";
  birthyear.value = "";
  btn.innerHTML = "Submit";
  btn.className = "btn btn-success";
}

$(document).ready(function () {
  randomEntry();
  getEntries();
});

let btn = document.getElementById("submitbtn");
btn.addEventListener("click", function (e) {
  send(btn);
});
