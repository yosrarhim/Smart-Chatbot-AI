document.getElementById('send').onclick = async ()=>{
const q = document.getElementById('question').value
const resp = await fetch('/api/chat', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({question:q})})
const j = await resp.json()
document.getElementById('answer').innerText = JSON.stringify(j, null, 2)
}