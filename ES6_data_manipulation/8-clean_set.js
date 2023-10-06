export default function cleanSet(setPara, startString) {
  const resultArr = [];
  if (startString !== '' || (startString instanceof String) || startString !== null) {
    for (const elem of setPara) {
      if (elem !== undefined && elem.startsWith(startString)) {
        const newElem = elem.replace(startString, '');
        resultArr.push(newElem);
      }
    }
    const resultString = resultArr.join('-');
    return resultString;
  }
  return '';
}
