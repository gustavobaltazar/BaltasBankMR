import { Inputs } from "./Inputs"
import { useState } from "react"
import { validatePassword } from "../../Utils/Validators"
import { tryLogin } from "../../fetchers/user"
import { useMutation } from "@tanstack/react-query"
import { useNavigate } from "react-router-dom"

export const CardLogin = () => {
    const navigate = useNavigate()
    const [loading, setLoading] = useState(false)
    const [form, setForm] = useState({
        cpf: '',
        senha: ''
    })

    const tryLoginMutation = useMutation(tryLogin, {
        onSuccess: (data, context, variables) => {
            if(data.status){
                console.log('logou')
            }
        }
    })


    const handleSubmit = async () => {
        event?.preventDefault()
        tryLoginMutation.mutate(form)
    }
    const handleChange = (event: any) => {
        setForm({ ...form, [event.target.name]: event.target.value })
    }

    const validateInput = () => {
        return validatePassword(form.senha)
    }

    console.log('Form está válido?', validateInput())

    return (
        <div className="text-center h-screen flex justify-center items-center">
            <div className="bg-escurinho p-24 md:p-36 text-center text-white dark:bg-white inline-block rounded-lg">
                <h1 className="text-white text-2xl dark:text-black mb-8">Faça seu login</h1>
                <div className="flex flex-col w-48 gap-6 justify-center items-center">
                    <Inputs username="CPF" type="text" placeholder="John Doe" onChange={handleChange} name="cpf" />
                    <Inputs username="Senha" type="password" placeholder="123" onChange={handleChange} name="senha" />
                    <div className="flex gap-8">
                        <button type="submit" onClick={handleSubmit} disabled={loading === true || !validateInput()} className={`${validateInput() === true ? "botao" : "botao_invalido"}`}>Login</button>
                        <a className="text-maincolor" href="/RegisterPage">Não possuo uma conta!</a>
                    </div>
                    <div id="renderResults" className="text-black">bolas</div>
                </div>
            </div>
        </div>
    )
}