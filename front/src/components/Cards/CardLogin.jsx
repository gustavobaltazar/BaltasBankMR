import { Inputs } from "./Inputs"
import { useState } from "react"
import { validatePassword } from "../../Utils/Validators"
export const CardLogin = () => {
    const [loading, setLoading] = useState()
    const [form, setForm] = useState([])

    const handleSubmit = async (event) => {
        event.preventDefault()
        try {
            setLoading(true)
            alert("Login")
            setLoading(false)
        } catch (err) {
            alert("Algo deu errado!")
        }
    }

    const handleChange = (event) => {
        console.log('Digitando...', event.target.name, event.target.value)
        setForm({ ...form, [event.target.name]: event.target.value })
        console.log("form", form)
    }

    const validateInput = () => {
        return validatePassword(form.password)
    }

    console.log('Form está válido?', validateInput())

    return (
        <div className="text-center h-screen flex justify-center items-center">
            <div className="bg-escurinho p-24 md:p-36 text-center text-white dark:bg-white inline-block rounded-lg">
                <h1 className="text-white text-2xl dark:text-black mb-8">Faça seu login</h1>
                <div className="flex flex-col w-48 gap-6 justify-center items-center">
                    <Inputs username="Usuário" type="text" placeholder="John Doe" onChange={handleChange} name="usuario" />
                    <Inputs username="Senha" type="password" placeholder="123" onChange={handleChange} name="password" />
                    <div className="flex gap-8">
                        <button href="#" type="submit" onClick={handleSubmit} disabled={loading === true | !validateInput()} className={`${validateInput() === true ? "botao" : "botao_invalido"}`}>Login</button>
                        <a className="text-maincolor" href="/RegisterPage">Não possuo uma conta!</a>
                    </div>
                </div>
            </div>
        </div>
    )
}