import { Link } from "react-router-dom";

import classes from "./ClothesItem.module.css";

const addIcon = (
  <img
    width="48"
    height="48"
    src="https://img.icons8.com/color/48/add--v1.png"
    alt="add--v1"
  />
);

const AddClothesItem = (props) => {
  return (
    <div className={classes["clothes-item"]}>
      <Link to="/clothes/new">{addIcon}</Link>
    </div>
  );
};

export default AddClothesItem;
