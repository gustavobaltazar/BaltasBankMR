import { Card } from "react-pay-card"
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
                    <p className="text-white text-2xl dark:text-black mb-8">Olá, {name}</p>
                    <div className="flex flex-col">
                        <span className="text-white text-2xl dark:text-black mb-8">R$ {wallet}</span>
                        {
                            creditCard && <Card cardCvv={creditCard.cvv} cardHolder={name} cardMonth={creditCard.validade.split("")[0] + creditCard.validade.split("")[1]} cardYear={creditCard.validade.split("")[3] + creditCard.validade.split("")[4]} cardNumber={creditCard.numero_cartao} />
                        }
                        <span className="text-white text-2xl dark:text-black mb-8">Tipo de conta: {accountType}</span>
                    </div>
                </div>
            </div>
        </div>
    )
}