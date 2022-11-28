interface InputsProps {
    type: any
    placeholder: string
    value?: any
    username: string
    onChange: React.ChangeEventHandler<HTMLInputElement>
    name: string
}

export const Inputs = ({ type, placeholder, value, username, onChange, name }: InputsProps) => {
    return (
        <div className="flex flex-col w-84 md:w-96">
            <span className="dark:text-black flex">{username}</span>
            <input className="input-style bg-escurinho border-none dark:bg-white focus:outline-none focus:shadow-outline" type={type} placeholder={placeholder} value={value} onChange={onChange} name={name} />
        </div>
    )
}