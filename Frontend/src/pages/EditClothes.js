import { useState } from "react";

import PageContent from "../components/PageContent";
import Dropdown from "../UI/Dropdown";
import Button from "../UI/Button";

const EditClothesPage = () => {
  const [selectedType, setSelectedType] = useState("");
  const [selectedColor, setSelectedColor] = useState("");
  const [selectedSeason, setSelectedSeason] = useState("");

  const handleTypeChange = (item) => {
    setSelectedType(item);
  };
  const handleColorChange = (item) => {
    setSelectedColor(item);
  };
  const handleSeasonChange = (item) => {
    setSelectedSeason(item);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("edit", selectedColor, selectedSeason, selectedType);
  };

  const handleDelete = () => {
    console.log("delete");
  };

  return (
    <PageContent>
      <form onSubmit={handleSubmit}>
        <h1>옷 수정하기</h1>
        <Dropdown items={["상의", "하의"]} onChange={handleTypeChange}>
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
        <Button color="red" type="button" onClick={handleDelete}>
          옷 삭제하기
        </Button>
        <Button type="submit">확인</Button>
      </form>
    </PageContent>
  );
};

export default EditClothesPage;

export const action = () => {};
