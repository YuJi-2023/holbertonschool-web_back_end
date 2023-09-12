export default function returnHowManyArguments(...theArgs) {
  let count = 0;
  for (let arg of theArgs) {
    count += 1;
  }
  return count;
}
