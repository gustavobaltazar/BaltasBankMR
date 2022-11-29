import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import axios from "axios";
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import { DarkMode } from "./components/DarkmodeControl/Darkmode";
import { Home } from "./pages/Home";
import { Login } from "./pages/Login";
import { Register } from "./pages/Register";
import { getManyUsers } from "./fetchers/user";

export function App() {
  const router = createBrowserRouter([
    {
      path: "/",
      element: <Home />,
    },
    {
      path: '/LoginPage',
      element: <Login />
    },
    {
      path: '/RegisterPage',
      element: <Register />
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