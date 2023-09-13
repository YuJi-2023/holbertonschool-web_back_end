export default function createEmployeesObject(departmentName, employees) {
  const NewEmploy = {
    [`${departmentName}`]: employees,
  };
  return NewEmploy;
}
