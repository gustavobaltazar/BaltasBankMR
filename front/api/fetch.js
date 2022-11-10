import axios from 'axios';
const url="http://localhost:8000/back/usuarios"

export function getUser(){
    axios.get(url)
    .then(response => {
        const data = response.data
    })
    .catch(error => console.log(error))
}