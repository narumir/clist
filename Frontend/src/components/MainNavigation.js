import { NavLink } from "react-router-dom";

import classes from "./MainNavigation.module.css";

const navItems = [
  { path: "/closet", text: "내 옷장" },
  { path: "/recommend", text: "옷 추천" },
  { path: "/login", text: "로그인" },
  { path: "/signup", text: "회원가입" },
];

function MainNavigation() {
  return (
    <header className={classes.header}>
      <nav>
        <ul className={classes.list}>
          {navItems.map((item) => (
            <li key={item.text}>
              <NavLink
                to={item.path}
                className={({ isActive }) =>
                  isActive ? classes.active : undefined
                }
              >
                {item.text}
              </NavLink>
            </li>
          ))}
        </ul>
      </nav>
    </header>
  );
}

export default MainNavigation;
