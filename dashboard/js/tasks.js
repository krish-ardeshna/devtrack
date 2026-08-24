const TASKS_URL = "https://raw.githubusercontent.com/krish-ardeshna/devtrack/main/tasks.json";

export async function fetchTasks() {
    const response = await fetch(TASKS_URL);
    if (!response.ok) {
        throw new Error(`Failed to fetch tasks: ${response.status} ${response.statusText}`);
    }
    
    const text = await response.text();
    if (!text.trim()) {
        return [];
    }
    
    return JSON.parse(text);
}