import { USE_LOCAL_API, LOCAL_API_BASE, GITHUB_OWNER, GITHUB_REPO, GITHUB_BRANCH } from "./config.js";

const RAW_TASKS_URL = `https://raw.githubusercontent.com/${GITHUB_OWNER}/${GITHUB_REPO}/${GITHUB_BRANCH}/tasks.json`;

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