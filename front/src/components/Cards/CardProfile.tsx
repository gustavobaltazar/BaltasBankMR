import { Card } from "react-pay-card"
import { User } from "phosphor-react"

interface CardProfileProps {
    name: string | 'UNNAMED'
    accountType: string | undefined
    wallet: number | undefined
    creditCard?: any
}

export function CardProfile({ name, accountType, wallet, creditCard }: CardProfileProps) {
    return (
        <div>
            <div className="text-center h-screen flex justify-center items-center">
                <div className="bg-escurinho p-24 md:p-36 text-center text-white dark:bg-white inline-block rounded-lg">
                    <div className="flex flex-row justify-center items-center gap-4">
                        <User size={48} color="#8257E5" weight="fill" />
                        <p className="text-white text-2xl dark:text-black">Olá, {name}</p>
                    </div>
                    <div className="flex flex-col gap-2">
                        <span className="text-white text-2xl dark:text-black">R$ {wallet}</span>
                        <span className="text-white text-2xl dark:text-black">Conta: {accountType == "G" ? "Gold" : accountType == "N" ? "Normal" : accountType == "P" ? "Platinum" : ""}</span>
                        {
                            creditCard && <Card cardCvv={creditCard.cvv} cardHolder={name} cardMonth={creditCard.validade.split("")[0] + creditCard.validade.split("")[1]} cardYear={creditCard.validade.split("")[3] + creditCard.validade.split("")[4]} cardNumber={creditCard.numero_cartao} />
                        }

                    </div>
                </div>
            </div>
        </div>
    )
}