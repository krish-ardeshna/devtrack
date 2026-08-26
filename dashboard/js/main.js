import { fetchRepoInfo, fetchCommits } from "./github.js";
import { fetchTasks } from "./tasks.js";
import { renderRepoInfo, renderTaskStats, renderTasks, renderCommits } from "./render.js";

async function init() {
    try {
        const repo = await fetchRepoInfo();
        const commits = await fetchCommits();
        const tasks = await fetchTasks();

        renderRepoInfo(repo);
        renderTaskStats(tasks);
        renderTasks(tasks, commits);
        renderCommits(commits);
    } catch (error) {
        console.error(error);
    }
}

document.addEventListener("DOMContentLoaded", init);