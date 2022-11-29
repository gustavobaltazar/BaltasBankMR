import axios from 'axios';
const url = "http://localhost:8000"
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

// function getUser() {
//     axios.get(url)
//         .then(response => {
//             const data = response.data
//             renderResults.textContent = JSON.stringify(data)
//         })
//         .catch(error => console.log(error))
// }

export async function addNewUser(userData: any) {
    axios.post(`${url}/usuarios/`, userData)
    .then(response => {
        return(JSON.stringify(response.data))
    })
    .catch(err => console.log(err)) 
}

export async function tryLogin(userData: any) {
    try{
        const res = await axios.post(`${url}/login/`, userData)
        return res.data
    }catch(err: any){
        return err.response.data
    }
}

export async function getOneUser(cpf: string){
    const res = await axios.get(`${url}/usuarios/${cpf}`)

    return res
}



