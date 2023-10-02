import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const firstPromise = uploadPhoto();
  const secondPromise = createUser();

  return Promise.all([firstPromise, secondPromise])
    .then(([firstResponse, secondResponse]) => {
      console.log(`${firstResponse.body} ${secondResponse.firstName} ${secondResponse.lastName}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
