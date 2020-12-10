console.log("huzzah!");

const populateTimes = (selectElement, choices) => {
  for (let choice of choices) {
    let opt = document.createElement("option");
    opt.innerHTML = choice;
    opt.value = choice;
    selectElement.appendChild(opt);
  }
};

const wakeHour = document.querySelector("#wakeup-hour");
const wakeMinutes = document.querySelector("#wakeup-minute");
console.log(wakeHour);

const hours = [];
for (let i = 0; i < 24; i++) {
  hours.push(i);
}

const minutes = [];
for (let i = 0; i < 60; i++) {
  minutes.push(i);
}

populateTimes(wakeHour, hours);
populateTimes(wakeMinutes, minutes);
