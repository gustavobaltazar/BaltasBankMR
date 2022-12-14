import { MdDarkMode } from "react-icons/md";
import { BsFillSunFill } from "react-icons/bs";
import { useTheme } from "../components/DarkmodeControl/Darkmode";
import { CardProfile } from "../components/Cards/CardProfile";
import { useLoaderData } from "react-router-dom";
import { useUserStore } from "../stores/user";

export function Profile() {
  const { theme, setTheme }: any = useTheme();
  const [user] = useUserStore((state) => [state.user])
  const card = useLoaderData()

  return (
    <>
      <div className="flex justify-between items-center">
        <a href="/">
          <img src="/baltas-bank-logo-reduzida.png" className="absolute left-0 h-44 shrink-0 md:select-none" />
        </a>
        <div className="absolute right-0 top-16 mr-4 mt-1 text-center h-16 w-16 md:select-none">
          {theme === "light" ? (
            <MdDarkMode
              size={30}
              className="cursor-pointer"
              onClick={() => setTheme("dark")}
            />
          ) : (
            <BsFillSunFill
              size={30}
              className="cursor-pointer text-white"
              onClick={() => setTheme("light")}
            />
          )}
        </div>
      </div>

      <CardProfile name={user?.nome!} accountType={user?.tipo_conta} wallet={user?.saldo} creditCard={card!.data[0]} />
    </>
  );
} 