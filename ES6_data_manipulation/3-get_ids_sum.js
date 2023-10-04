export default function getStudentIdsSum(studentList) {
  const idList = studentList.map((student) => student.id);
  const resultSum = idList.reduce((accumulator, id) => accumulator + id);
  return resultSum;
}
