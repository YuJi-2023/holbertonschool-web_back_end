export default class HolbertonCourse {
  constructor(name, length, students) {
    this.setName(name);
    this.setLength(length);
    this.setStudents(students);
  }

  getName() {
    return this._name;
  }

  getLength() {
    return this._length;
  }

  getStudents() {
    return this._students;
  }

  setName(name) {
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = name;
  }

  setLength(length) {
    if (typeof length !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = length;
  }

  setStudents(students) {
    if (!Array.isArray(students) || !students.every((student) => typeof student === 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    this._students = students;
  }

  set name(newName) {
    this.setName(newName);
  }

  set length(newLength) {
    this.setLength(newLength);
  }

  set students(newStudents) {
    this.setStudents(newStudents);
  }
}
