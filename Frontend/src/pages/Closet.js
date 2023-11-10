import AddClothesItem from "../components/AddClothesItem";
import ClothesList from "../components/ClothesList";
import PageContent from "../components/PageContent";

const DUMMY_CLOTHES_DATA = [
  {
    clothes_id: 1,
    color: "red",
    is_upper: true,
    season: "winter",
    state: undefined,
  },
  {
    clothes_id: 2,
    color: "yellow",
    is_upper: false,
    season: "summer",
    state: undefined,
  },
  {
    clothes_id: 3,
    color: "blue",
    is_upper: true,
    season: "spring",
    state: undefined,
  },
  {
    clothes_id: 4,
    color: "red",
    is_upper: true,
    season: "winter",
    state: undefined,
  },
  {
    clothes_id: 5,
    color: "yellow",
    is_upper: false,
    season: "summer",
    state: undefined,
  },
  {
    clothes_id: 6,
    color: "blue",
    is_upper: true,
    season: "spring",
    state: undefined,
  },
];

const ClosetPage = () => {
  return (
    <PageContent width="max-content">
      <ClothesList clothesData={DUMMY_CLOTHES_DATA}>
        <AddClothesItem />
      </ClothesList>
    </PageContent>
  );
};

export default ClosetPage;

export const loader = () => {};
