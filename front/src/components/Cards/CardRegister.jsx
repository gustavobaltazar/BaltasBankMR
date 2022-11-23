import { Inputs } from "./Inputs"
import { useState } from "react";
import { addNewUser } from "../../../api/fetch"

export const CardRegister = () => {
    const [inputs, setInputs] = useState({
        cpf: "",
        email:"",
        senha: ""
    });
    const [message, setMessage] = useState("");

    const emailValidation = () => {
        const regEx = /[a-zA-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,8}(.[a-z{2,8}])?/g
        if (regEx.test(inputs.email)) {
            setMessage("Email válido")
        } else if (!regEx.test(inputs.email) && inputs.email != "") {
            setMessage("Email inválido")
        } else {
            setMessage("")
        }
    }

    const handleOnChange = (e) => {
        setInputs({
            ...inputs,
            [e.target.name]: e.target.value
        })
    }

    function handleSubmit(){
        event.preventDefault()
        addNewUser(inputs)
        console.log(inputs)
    }

    return (
        <div>
            <div className="text-center h-screen flex justify-center items-center">
                <div className="bg-escurinho p-24 md:p-36 text-center text-white dark:bg-white inline-block rounded-lg">
                    <h1 className="text-white text-2xl dark:text-black mb-8">Crie sua conta</h1>
                    <form onSubmit={handleSubmit} className="flex flex-col w-48 gap-6 justify-center items-center">
                        <Inputs username="Usuário" type="text" placeholder="Usuário" name="cpf" value={inputs.user} onChange={(event) => handleOnChange(event)} />
                        <Inputs username="Email" type="email" placeholder="Email" name="email" value={inputs.email} onChange={(event) => handleOnChange(event)} />
                        <Inputs username="Senha" type="password" placeholder="Senha" name="senha" value={inputs.password} onChange={(event) => handleOnChange(event)} />

                        <div className="flex gap-8">

                            <button type="submit" className="w-32 h-10 text-white rounded-full transition-all duration-[500ms] bg-gradient-to-tl from-pink-500 via-maincolor to-maincolor bg-size-200 bg-pos-0 hover:bg-pos-100 text-center py-2" >Register</button>
                            <a className="text-maincolor" href="/LoginPage">Já possuo uma conta!</a>

                        </div>
                        <div className="text-maincolor text-3xl">{message}</div>
                    </form>
                </div>
            </div>
        </div>
    )
}