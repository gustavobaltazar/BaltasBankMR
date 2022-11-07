const validatePassword = (password) => {
    return password?.toString().length > 6
}

export {
    validatePassword
}