export default function cleanSet(setPara, startString) {
  const resultArr = [];
  if (startString === '' || (typeof startString !== 'string') || startString === null) {
    return '';
  }
  for (const elem of setPara) {
    if (elem !== undefined && elem.startsWith(startString)) {
      const newElem = elem.replace(startString, '');
      resultArr.push(newElem);
    }
  }
  const resultString = resultArr.join('-');
  return resultString;
}
