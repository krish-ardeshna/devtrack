import { USE_LOCAL_API, LOCAL_API_BASE } from "./config.js";

const RAW_REPO_URL = "https://api.github.com/repos/krish-ardeshna/devtrack";
const RAW_COMMITS_URL = "https://api.github.com/repos/krish-ardeshna/devtrack/commits?per_page=5";

export async function fetchRepoInfo() {
    const url = USE_LOCAL_API ? `${LOCAL_API_BASE}/github/repo/` : RAW_REPO_URL;
    const response = await fetch(url);
    if(!response.ok) {
        throw new Error(`Failed to fetch repo info ${response.status} ${response.statusText}`);
    }
    return await response.json();
 }

export async function fetchCommits() {
    const url = USE_LOCAL_API ? `${LOCAL_API_BASE}/github/commits` : RAW_COMMITS_URL;
    const response = await fetch(url)
    if(!response.ok) {
        throw new Error(`Failed to fetch commits: ${response.status} ${response.statusText}`);
    }
    return await response.json();
}