import { useState } from "react";
import classes from "./Dropdown.module.css";
import icon from "./expand-arrow.png";

const Dropdown = (props) => {
  const [currItem, setCurrItem] = useState(null);
  const [isOpened, setIsOpened] = useState(false);

  return (
    <div className={classes.dropdown}>
      <button
        className={`${classes.dropbtn} ${currItem ? classes.active : ""}`}
        onClick={() => setIsOpened(!isOpened)}
        type="button"
      >
        {currItem ? currItem : props.children}
        <img src={icon} alt={"expand-arrow"} className={classes.icon} />
      </button>
      <ul className={classes["dropdown-content"]}>
        {isOpened &&
          props.items.map((item) => (
            <li
              key={item}
              value={item}
              onClick={() => {
                setCurrItem(item);
                setIsOpened(false);
                props.onChange(item);
              }}
            >
              {item}
            </li>
          ))}
      </ul>
    </div>
  );
};

export default Dropdown;
