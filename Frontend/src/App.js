import { createBrowserRouter, RouterProvider } from "react-router-dom";

import classes from "./App.module.css";
import RootPage from "./pages/Root";
import LoginPage from "./pages/Login";
import SignupPage from "./pages/Signup";
import ClosetPage from "./pages/Closet";
import RecommendPage from "./pages/Recommend";
import EditClothesPage from "./pages/EditClothes";
import NewClothesPage from "./pages/NewClothes";
import ErrorPage from "./pages/Error";

const router = createBrowserRouter([
  {
    path: "/",
    element: <RootPage />,
    errorElement: <ErrorPage />,
    children: [
      { path: "login", element: <LoginPage /> },
      { path: "signup", element: <SignupPage /> },
      { path: "closet", element: <ClosetPage /> },
      { path: "recommend", element: <RecommendPage /> },
      {
        path: "clothes",
        children: [
          { path: ":clothesId/edit", element: <EditClothesPage /> },
          { path: "new", element: <NewClothesPage /> },
        ],
      },
    ],
  },
]);
const App = () => {
  return (
    <div className={classes.App}>
      <RouterProvider router={router} />
    </div>
  );
};

export default App;
