export default function divideFunction(numerator, denominator) {
  if (denominator === 0) {
    throw Error('cannot divide by 0');
  }
  return numerator / denominator;
}

try {
  const numerator = 10;
  const denominator = 2;
  divideFunction(numerator, denominator);
} catch (e) {
  console.error(e.message);
}
