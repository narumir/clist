import { useState } from "react";

import Button from "../UI/Button";
import Dropdown from "../UI/Dropdown";
import PageContent from "../components/PageContent";

const NewClothesPage = () => {
  const [selectedIsUpper, setSelectedIsUpper] = useState("");
  const [selectedColor, setSelectedColor] = useState("");
  const [selectedSeason, setSelectedSeason] = useState("");

  const handleIsUpperChange = (item) => {
    setSelectedIsUpper(item);
  };
  const handleColorChange = (item) => {
    setSelectedColor(item);
  };
  const handleSeasonChange = (item) => {
    setSelectedSeason(item);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("add", selectedColor, selectedSeason, selectedIsUpper);
  };

  return (
    <PageContent>
      <form onSubmit={handleSubmit}>
        <h1>옷 추가하기</h1>
        <Dropdown items={["상의", "하의"]} onChange={handleIsUpperChange}>
          종류 선택
        </Dropdown>
        <Dropdown items={["빨강", "노랑", "파랑"]} onChange={handleColorChange}>
          색상 선택
        </Dropdown>
        <Dropdown
          items={["여름", "겨울", "봄/가을"]}
          onChange={handleSeasonChange}
        >
          계절 선택
        </Dropdown>
        <Button type="submit">확인</Button>
      </form>
    </PageContent>
  );
};

export default NewClothesPage;

export const action = () => {};
