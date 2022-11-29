const validatePassword = (password: string) => {
    return password?.toString().length > 2
}

export {
    validatePassword
}