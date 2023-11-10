import classes from "./Button.module.css";

const Button = (props) => {
  return (
    <div>
      <button
        type={props.type}
        className={`${classes.button} ${
          props.color === "red" ? classes.red : ""
        }`}
        onClick={props.onClick}
      >
        {props.children}
      </button>
    </div>
  );
};

export default Button;
