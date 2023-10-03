export default function guardrail(mathFunction) {
  const queue = [];
  const defaultMessage = 'Guardrail was processed';

  try {
    const result = mathFunction();
    queue.push(result);
    queue.push(defaultMessage);
  } catch (e) {
    queue.push(`Error: ${e.message}`);
    queue.push(defaultMessage);
  }
  return queue;
}
