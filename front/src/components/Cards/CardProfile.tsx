export function CardProfile({ name = "", accountType = "", wallet = "", creditCard = "" }) {
    return (
        <div>
            <div className="text-center h-screen flex justify-center items-center">
                <div className="bg-escurinho p-24 md:p-36 text-center text-white dark:bg-white inline-block rounded-lg">
                    <p className="text-white text-2xl dark:text-black mb-8">Olá, {name}</p>
                    <div className="flex flex-col">
                        <span className="text-white text-2xl dark:text-black mb-8">R$ {wallet}</span>
                        <span className="text-white text-2xl dark:text-black mb-8">Limite: {creditCard}</span>
                        <span className="text-white text-2xl dark:text-black mb-8">Tipo de conta: {accountType}</span>
                    </div>
                </div>
            </div>
        </div>
    )
}