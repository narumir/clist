import classes from "./PageContent.module.css";

const PageContent = (props) => {
  return (
    <div className={classes.container}>
      <div
        className={`${classes.content} ${
          props.width === "max-content" ? classes["max-content"] : ""
        }`}
      >
        {props.children}
      </div>
    </div>
  );
};

export default PageContent;
