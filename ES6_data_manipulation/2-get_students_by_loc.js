export default function getStudentsByLocation(studentList, City) {
  const resultList = studentList.filter((student) => student.location === City);
  return resultList;
}
