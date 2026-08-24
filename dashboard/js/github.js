const REPO_URL = "httpsL//api.github.com/repos/krish-ardeshna/devtrack"

export async function fetchRepInfo() {
    const response = await fetch(REPO_URL);
    if(!response.ok) {
        throw new Error(`Failed to fetch repo info: ${response.status} ${response.statusText}`)
    }
    return await response.json();
}