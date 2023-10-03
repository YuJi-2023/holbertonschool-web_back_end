import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const promise1 = signUpUser(fileName, lastName);
  const promise2 = uploadPhoto(fileName);

  return Promise.all([promise1, promise2])
    .then(([result1, result2]) => [result1.status, result1.value, result2.status, result2.value]);
}
