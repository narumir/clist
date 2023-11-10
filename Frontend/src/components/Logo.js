import logo from "./logo.png";

import classes from "./Logo.module.css";

const Logo = () => {
  return (
    <div className={classes.logo}>
      <img src={logo} alt="clist-logo" />
      <p>
        icon by <a href="https://icons8.com/">icons8</a>
      </p>
    </div>
  );
};

export default Logo;
