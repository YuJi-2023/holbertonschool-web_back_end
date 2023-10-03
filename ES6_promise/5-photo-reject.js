export default function uploadPhoto(filename) {
  const errorMessage = `${filename} cannot be processed`;
  return new Promise((resolve, reject) => {
    reject(new Error(errorMessage));
  });
}
