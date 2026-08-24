import { fetchTasks } from "./tasks.js";
import { fetchRepoInfo, fetchCommits } from "./github.js";
import { renderTasks, renderRepoInfo, renderCommits } from "./render.js";

async function init() {
    try {
        const [tasks, repo, commits] = await Promise.all([
            fetchTasks(),
            fetchRepoInfo(),
            fetchCommits()
        ]);
        
        renderRepoInfo(repo);
        renderCommits(commits);
        renderTasks(tasks, commits);
    } catch (error) {
        console.error("Dashboard failed to load data:", error);
    }
}

document.addEventListener("DOMContentLoaded", init);