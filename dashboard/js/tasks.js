const TASKS_URL = "https://raw.githubusercontent.com/krish-ardeshna/devtrack/main/tasks.json"

export async function fetchTasks() {
    const response = await fetch(TASKS_URL);
    if(!response.ok) {
        throw new Error(`Failed to fetch tasks: ${response.status} ${response.statusText}`)
    }
    return await response.json();
}

