const customStartTime = new Date();
const model = "AXON BODY 3";
const serial = "X" + Math.floor(10000000 + Math.random() * 89999999);

document.getElementById("line2").innerText = `${model} ${serial}`;

function updateTime() {
  const now = new Date();
  const elapsed = now - customStartTime;
  const current = new Date(customStartTime.getTime() + elapsed);

  const tzOffset = current.getTimezoneOffset() / -60;
  const sign = tzOffset >= 0 ? "+" : "-";
  const formatted = current.getFullYear() + "-" +
    String(current.getMonth()+1).padStart(2, '0') + "-" +
    String(current.getDate()).padStart(2, '0') + " " +
    String(current.getHours()).padStart(2, '0') + ":" +
    String(current.getMinutes()).padStart(2, '0') + ":" +
    String(current.getSeconds()).padStart(2, '0') + " " +
    sign + String(Math.abs(tzOffset)).padStart(2, '0') + "00";

  document.getElementById("line1").innerText = formatted;
}

setInterval(updateTime, 1000);
updateTime();
