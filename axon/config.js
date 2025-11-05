const customStartTime = new Date(2012, 11, 12, 23, 5, 49);
const model = "AXON BODY 3";
const serial = "X" + Math.floor(10000000 + Math.random() * 89999999);

function updateTime() {
  const current = customStartTime; 
  customStartTime.setSeconds(customStartTime.getSeconds() + 1); 

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
  document.getElementById("line2").innerText = `${model} ${serial}`;
}

setInterval(updateTime, 1000);
updateTime();
