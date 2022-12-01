import axios from 'axios';
const url = "http://localhost:8000"

export async function addNewUser(userData: any) {
    axios.post(`${url}/usuarios/`, userData)
        .then(response => {
            return (JSON.stringify(response.data))
        })
        .catch(err => console.log(err))
}

export async function tryLogin(userData: any) {
    try {
        const res = await axios.post(`${url}/login/`, userData)
        return res.data
    } catch (err: any) {
        return err.response.data
    }
}

export function getOneUser(cpf: string) {
    return axios.get(`${url}/usuarios/${cpf}`)
}

export function getUserCard(cpf: string) {
    return axios.post(`${url}/pega_cartao/`, { usuario: cpf })

}



