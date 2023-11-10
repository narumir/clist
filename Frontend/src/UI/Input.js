import classes from "./Input.module.css";

const Input = (props) => {
  return (
    <div>
      <input
        className={classes.input}
        placeholder={props.placeholder}
        onChange={props.onChange}
        id={props.id}
      >
        {props.children}
      </input>
    </div>
  );
};

export default Input;
