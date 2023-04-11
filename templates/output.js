const x = {{s|tojson}}
console.log(x)
// document.getElementById("div").innerHTML = x[0]

const div = document.getElementById("div")

for (let index = 0; index < x.length; index++) {
  let skillToImprove = document.createElement("div")
  skillToImprove.textContent = x[index]

  div.append(skillToImprove)
  
