import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const promise1 = signUpUser(firstName, lastName);
  const promise2 = uploadPhoto(fileName);

  // return Promise.all([promise1, promise2].map((p) => p.then((result) => ({
  //   status: 'fulfilled',
  //   value: result,
  // })).catch((e) => ({ status: 'rejected', value: `Error: ${e.message}` }))));
  return Promise.allSettled([promise1, promise2]).then((results) => results.map((result) => ({
    status: result.status,
    value: result.status === 'fulfilled' ? result.value : result.reason,
  })));
}
