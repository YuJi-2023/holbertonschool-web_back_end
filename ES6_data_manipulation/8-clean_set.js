export default function cleanSet(setPara, startString) {
  const resultArr = [];
  if (startString !== '') {
    for (const elem of setPara) {
      if (elem.includes(startString)) {
        const newElem = elem.replace(startString, '');
        resultArr.push(newElem);
      }
    }
    const resultString = resultArr.join('-');
    return resultString;
  }
  return '';
}
