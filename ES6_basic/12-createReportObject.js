export default function createReportObject(employeesList) {
  const reportResult = {
    allEmployees: employeesList,
    getNumberOfDepartments(employeesList) {
      return Object.keys(employeesList).length;
    },
  };
  return reportResult;
}
