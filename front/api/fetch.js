import axios from 'axios';
const url = "http://localhost:8000/back/usuarios/"
const newUser = {
    cpf: "99999999999",
    email: "bubas@gmail.com",
    senha: "9834",
}
    
const updatedUser = {
    cpf: "88888888888",
    email: "bebas@gmail.com",
    senha: "8787",
}

function getUser() {
    axios.get(url)
        .then(response => {
            const data = response.data
            renderResults.textContent = JSON.stringify(data)
        })
        .catch(error => console.log(error))
}


export function addNewUser(userData) {
    axios.post(url, userData)
    .then(response => {
        alert(JSON.stringify(response.data))
    })
    .catch(err => console.log(err)) 
}
// addNewUser()

function updateUser() {
    axios.put(url, updatedUser)
    .then(response => {})
    .catch(err => console.log(err))
}



