export default function createInt8TypedArray(length, position, value) {
  const myArrayBuffer = new ArrayBuffer(length);
  const myDataView = new DataView(myArrayBuffer);

  // check position range
  if (position < 0 || position >= length) {
    throw Error('Position outside range');
  }
  myDataView.setInt8(position, value);
  return myDataView;
}
