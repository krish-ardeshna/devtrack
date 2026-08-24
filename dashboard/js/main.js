import { fetchTasks } from './tasks.js'
import { fetchRepoInfo, fetchCommits } from './github.js'
import { renderRepoInfo, renderCommits, renderTasks } from './render.js'

async function init() {
    try {
        const [tasks, repo, commits] = await Promise.all([
            fetchTasks(),
            fetchRepoInfo(),
            fetchCommits()
        ]);

        renderTasks(tasks);
        renderRepoInfo(repo);
        renderCommits(commits);
    } catch (error) {
        console.error("Dashboard failed to load data:", error);
    }
}

document.addEventListener('DOMContentLoaded', init);