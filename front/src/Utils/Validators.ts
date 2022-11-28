const validatePassword = (password: string) => {
    return password?.toString().length > 6
}

export {
    validatePassword
}