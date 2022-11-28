import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import { DarkMode } from "./components/DarkmodeControl/Darkmode";
import { Home } from "./pages/Home";
import { Login } from "./pages/Login";
import { Register } from "./pages/Register";

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

  return (<DarkMode><RouterProvider router={router} /></DarkMode>)
}