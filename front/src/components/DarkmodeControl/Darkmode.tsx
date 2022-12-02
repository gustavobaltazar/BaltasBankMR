import { useState, useContext, createContext, useEffect } from "react";
const themeContext = createContext<Context | undefined>({ theme: 'light', setTheme: undefined });

export interface Context {
  theme: any;
  setTheme: React.Dispatch<React.SetStateAction<string>> | undefined;
}

interface DarkModeProps {
  children: any
}


export function DarkMode({ children }: DarkModeProps) {
  const [theme, setTheme] = useState(
    localStorage.getItem("theme") !== "dark" ? "light" : "dark"
  );

  useEffect(() => {
    const root = window.document.documentElement;
    const removeOldTheme = theme === "dark" ? "light" : "dark";

    root.classList.remove(removeOldTheme);
    root.classList.add(theme);
    localStorage.setItem("theme", theme);
  }, [theme]);
  return (
    <themeContext.Provider value={{ theme, setTheme }}>
      {children}
    </themeContext.Provider>
  );
};

export function useTheme() {
  return useContext(themeContext);
}
