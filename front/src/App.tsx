import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import {
  createBrowserRouter,
  redirect,
  RouterProvider,
} from "react-router-dom";
import { DarkMode } from "./components/DarkmodeControl/Darkmode";
import { Home } from "./pages/Home";
import { Login } from "./pages/Login";
import { Register } from "./pages/Register";
import { Profile } from "./pages/Profile";
import { useUserStore } from "./stores/user";
import { getUserCard } from "./fetchers/user";
// import { getManyUsers } from "./fetchers/user";

export function App() {
  const [user] = useUserStore((state) => [state.user])
  const router = createBrowserRouter([
    {
      path: "/",
      element: <Home />,
    },
    {
      path: '/LoginPage',
      element: <Login />,
      loader: () => {
        if (user) return redirect(`/`)
      }
    },
    {
      path: '/RegisterPage',
      element: <Register />,
      loader: () => {
        if (user) return redirect(`/`)
      }
    },
    {
      path: '/ProfilePage/:id',
      element: <Profile />,
      loader: () => {
        if (!user) return redirect(`/`)
        else return getUserCard(user.cpf).then((data) => data)
      }
    }
  ]);

  const queryClient = new QueryClient

  return (
    <DarkMode>
      <QueryClientProvider client={queryClient}>
        <RouterProvider router={router} />
      </QueryClientProvider>
    </DarkMode>
  )
}