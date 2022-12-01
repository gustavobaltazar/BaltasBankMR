import create from "zustand";
import { persist } from 'zustand/middleware';

interface User {
    cpf: string,
    email: string,
    senha: string,
    tipo_conta: string,
    saldo: number
}

interface UserStore {
    user: User | null;
    login: any
    logout: any
}

export const useUserStore = create<UserStore>()(persist((set) => ({
    user: null,
    login: (data: User) => set(() => ({ user: data })),
    logout: () => set(() => ({ user: null }))
}), {
    name: 'user-store',
    getStorage: () => localStorage
}
))