import axios from "axios";
import create from "zustand";
import { persist } from 'zustand/middleware';
import { url } from '../fetchers/user'

interface User {
    cpf: string,
    email: string,
    senha: string,
    tipo_conta: string,
    saldo: number,
    nome: string
}

interface UserStore {
    user: User | null
    login: (cpf: string) => void
    logout: () => void
}

export const useUserStore = create<UserStore>()(persist((set) => ({
    user: null,
    login: async (cpf) => {
        const { data } = await axios.get(`${url}/usuarios/${cpf}`)
        set(() => ({ user: data }))
    },
    logout: () => set(() => ({ user: null })),
}), {
    name: 'user-store',
    getStorage: () => localStorage
}
))