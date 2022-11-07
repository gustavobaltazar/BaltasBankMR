import { Inputs } from "./Inputs"
import { useState } from "react"
import { validatePassword } from "../../Utils/Validators"
export const CardLogin = () => {
    const [loading, setLoading] = useState()
    const [form, setForm] = useState()

    const validateInput = () => {
        return validatePassword(form.password)
    }

    console.log(validateInput)
    const handleSubmit = async (event) => {
        event.preventDefault()
        try{
            setLoading(true)
            alert("Login")
            setLoading(false)
        }catch(err){
            alert("Algo deu errado!")
        }
    }
    
    const handleChange = (event) => {
        console.log('Digitando...', event.target.name, event.target.value)
        setForm({...form, [event.target.name] : event.target.value})
        console.log("form", form)
    }
    console.log(validateInput)
    return (
        <div className="text-center h-screen flex justify-center items-center">
            <div className="bg-escurinho p-24 md:p-36 text-center text-white dark:bg-white inline-block rounded-lg">
                <h1 className="text-white text-2xl dark:text-black mb-8">Faça seu login</h1>
                <div className="flex flex-col w-48 gap-6 justify-center items-center">
                    <Inputs username="Usuário" type="text" placeholder="Usuário" onChange={handleChange} name="usuario"/>
                    <Inputs username="Senha" type="password" placeholder="Senha" onChange={handleChange} name="senha"/>
                    <div className="flex gap-8">
                        <button href="#" type="submit" onClick={handleSubmit} className="w-32 h-10 text-white rounded-full transition-all duration-[500ms] bg-gradient-to-tl from-pink-500 via-maincolor to-maincolor bg-size-200 bg-pos-0 hover:bg-pos-100 text-center py-2">Login</button>
                        <a className="text-maincolor" href="/RegisterPage">Não possuo uma conta!</a>
                    </div>
                </div>
            </div>
        </div>
    )
}