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
      throw new Error('Name must be a string');
    }
    this._name = name;
  }

  setLength(length) {
    if (typeof length !== 'number') {
      throw new Error('Length must be a number');
    }
    this._length = length;
  }

  setStudents(students) {
    if (!Array.isArray(students) || !students.every((student) => typeof student === 'string')) {
      throw new Error('Students must be an array of strings');
    }
    this._students = students;
  }
}
