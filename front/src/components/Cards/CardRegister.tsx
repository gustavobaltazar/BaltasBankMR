import { Inputs } from "./Inputs"
import { useState } from "react";
import { useMutation } from "@tanstack/react-query";
import { addNewUser } from "../../fetchers/user"
import { Notify } from 'notiflix'
export const CardRegister = () => {
    const [inputs, setInputs] = useState({
        cpf: "",
        nome: "",
        email: "",
        senha: "",
    });
    const [message, setMessage] = useState("");

    const postDataMutation = useMutation(addNewUser, {
        onSuccess: () =>{
            Notify.success('Logado!', { timeout: 2000 });
        }
    })

    const handleOnChange = (e: any) => {
        setInputs({
            ...inputs,
            [e.target.name]: e.target.value
        })
    }

    function handleSubmit() {
        event?.preventDefault()
        postDataMutation.mutate(inputs)
        console.log(inputs)
    }

    return (
        <div>
            <div className="text-center h-screen flex justify-center items-center">
                <div className="bg-escurinho p-24 md:p-36 text-center text-white dark:bg-white inline-block rounded-lg">
                    <h1 className="text-white text-2xl dark:text-black mb-8">Crie sua conta</h1>
                    <form onSubmit={handleSubmit} className="flex flex-col w-48 gap-6 justify-center items-center">
                        <Inputs username="Usuário" type="text" placeholder="CPF" name="cpf" value={inputs.cpf} onChange={(event) => handleOnChange(event)} />
                        <Inputs username="Nome" type="text" placeholder="Nome" name="nome" value={inputs.nome} onChange={(event) => handleOnChange(event)} />
                        <Inputs username="Email" type="email" placeholder="Email" name="email" value={inputs.email} onChange={(event) => handleOnChange(event)} />
                        <Inputs username="Senha" type="password" placeholder="Senha" name="senha" value={inputs.senha} onChange={(event) => handleOnChange(event)} />

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