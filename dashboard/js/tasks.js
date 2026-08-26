import { USE_LOCAL_API, LOCAL_API_BASE } from "./config.js";

const RAW_TASKS_URL = "https://raw.githubusercontent.com/krish-ardeshna/devtrack/main/tasks.json";

export async function fetchTasks() {
    const url = USE_LOCAL_API ? `${LOCAL_API_BASE}/tasks` : RAW_TASKS_URL;
    const response = await fetch(url);
    if(!response.ok) {
        throw new Error(`Failed to fetch tasks: ${response.status} ${response.statusText}`);
    } 

    const text = await response.text();
    if(!text.trim()) {
        return []; // Return an empty array if the response is empty
    }
    return JSON.parse(text);
}