export default function getListStudents() {
  const resultArray = new Array(3);
  const obj1 = {
    id: 1,
    firstName: 'Guillaume',
    location: 'San Francisco',
  };
  const obj2 = {
    id: 2,
    firstName: 'James',
    location: 'Columbia',
  };
  const obj3 = {
    id: 5,
    firstName: 'Serena',
    location: 'San Francisco',
  };

  resultArray[0] = obj1;
  resultArray[1] = obj2;
  resultArray[2] = obj3;
  return resultArray;
}
