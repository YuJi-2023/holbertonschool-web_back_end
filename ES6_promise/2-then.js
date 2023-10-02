export default function handleResponseFromAPI(promise) {
  const myPromise = new Promise((resolve, reject) => {
    if (promise) {
      resolve({
        status: 200,
        body: 'success',
      });
    } else {
      reject(new Error());
    }
  });
  myPromise
    .then((response) => {
      console.log('Got a response from the API');
      return response;
    });
  return myPromise;
}
