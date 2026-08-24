const REPO_URL = "https://api.github.com/repos/krish-ardeshna/devtrack"

export async function fetchRepoInfo() {
    const response = await fetch(REPO_URL);
    if(!response.ok) {
        throw new Error(`Failed to fetch repo info: ${response.status} ${response.statusText}`)
    }
    return await response.json();
}

const COMMITS_URL = "https://api.github.com/repos/krish-ardeshna/devtrack/commits?per_page=5"

export async function fetchCommits() {
    const response = await fetch(COMMITS_URL);
    if(!response.ok) {
        throw new Error(`Failed to fetch commits: ${response.status} ${response.statusText}`)
    }
    return await response.json();
}