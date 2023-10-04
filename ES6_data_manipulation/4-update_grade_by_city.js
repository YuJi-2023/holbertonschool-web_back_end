export default function updateStudentGradeByCity(studentList, city, newGrades) {
  const studentInCityList = studentList.filter((student) => student.location === city);

  return studentInCityList.map((student) => {
    const a = newGrades.find((grade) => grade.studentId === student.id);
    return {
      id: student.id,
      firstName: student.firstName,
      location: student.location,
      grade: a ? a.grade : 'N/A',
    };
  });
}
