export default function appendToEachArrayValue(array, appendString) {
  const newArray = [];
  let elem;
  for (elem of array) {
    newArray.push(appendString + elem);
  }

  return newArray;
}
