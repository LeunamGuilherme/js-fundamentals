// Exemplo simples em JavaScript para teste
const studentName = "Guilherme";
const currentModule = "JavaScript & TypeScript";
const isGitConfigured = true;

const completedTasks = [
  "Git & GitHub Setup",
  "VS Code Terminal Test",
  "First JS Code Executed"
];

function getStatusSummary(name, module, tasks) {
  return `Student: ${name} | Module: ${module} | Completed Steps: ${tasks.length}`;
}

console.log("=== TEST EXECUTION ===");
console.log(getStatusSummary(studentName, currentModule, completedTasks));

if (isGitConfigured) {
  console.log("Status: Ready to commit to GitHub!");
}