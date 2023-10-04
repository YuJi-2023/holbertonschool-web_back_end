export default function hasValuesFromArray(setPara, arrayPara) {
  const mySet = new Set(arrayPara);
  for (const elem of mySet) {
    if (!setPara.has(elem)) {
      return false;
    }
  }
  return true;
}
