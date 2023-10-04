export default function getStudentsByLocation(studentList, City) {

  const result = studentList.filter((student) => student.location === City);
  return result;
}
