import { useState } from "react";

import PageContent from "../components/PageContent";
import Button from "../UI/Button";
import Logo from "../components/Logo";
import Input from "../UI/Input";
import Dropdown from "../UI/Dropdown";

const locations = [
  "서울",
  "인천",
  "경기",
  "대전",
  "대구",
  "부산",
  "울산",
  "제주",
];

const SignupPage = () => {
  const [inputId, setInputId] = useState("");
  const [inputPw, setInputPw] = useState("");
  const [selectedLocation, setSelectedLocation] = useState("");

  const handleIdInputChange = (e) => {
    setInputId(e.target.value);
  };
  const handlePwInputChange = (e) => {
    setInputPw(e.target.value);
  };

  const handleLocationChange = (item) => {
    setSelectedLocation(item);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(inputId, inputPw, selectedLocation);
  };

  return (
    <PageContent>
      <Logo />
      <form onSubmit={handleSubmit} id="signup">
        <p>회원가입</p>
        <Input
          type="text"
          placeholder="아이디"
          onChange={handleIdInputChange}
          id="id"
        />
        <Input
          type="text"
          placeholder="비밀번호"
          onChange={handlePwInputChange}
          id="pw"
        />
        <Dropdown items={locations} onChange={handleLocationChange}>
          지역 선택하기
        </Dropdown>
        <Button type="submit">가입하기</Button>
      </form>
    </PageContent>
  );
};

export default SignupPage;

export const action = () => {};
