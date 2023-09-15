export default class HolbertonCourse {
  constructor(name, length, students) {
    this.setName(name);
    this.setLength(length);
    this.setStudents(students);
  }

  get name() {
    return this._name;
  }

  setName(name) {
    if (typeof name !== 'string') {
      throw TypeError('Name must be a string');
    }
    this._name = name;
  }

  set name(newName) {
    this.setName(newName);
  }

  get length() {
    return this._length;
  }

  setLength(length) {
    if (typeof length !== 'number') {
      throw TypeError('Length must be a number');
    }
    this._length = length;
  }

  set length(newLength) {
    this.setLength(newLength);
  }

  get students() {
    return this._students;
  }

  setStudents(students) {
    if (!Array.isArray(students) || !students.every((student) => typeof student === 'string')) {
      throw TypeError('Students must be an array of strings');
    }
    this._students = students;
  }

  set students(newStudents) {
    this.setStudents(newStudents);
  }
}
