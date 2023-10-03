export default function getListStudentIds(studentList) {
  if (Array.isArray(studentList)) {
    const result = studentList.map((student) => student.id);
    return result;
  }
  return [];
}
