export function renderRepoInfo(repo) {
    const container = document.getElementById("repo-stats");
    if(!container) return;

    container.innerHTML = "";

    const heading = document.createElement("h2");
    heading.textContent = repo.name;

    const desc = document.createElement("p");
    desc.textContent = repo.description || "No description";

    const stats = document.createElement("span");
    stats.textContent = `⭐ ${repo.stargazers_count}`;

    container.append(heading, desc, stats);
}

export function renderCommits(commits) {
    const container = document.getElementById("commits-list");
    if (!container) return;
    
    container.innerHTML = "";
    
    commits.forEach(commitData => {
        const div = document.createElement("div");
        div.className = "commit-item";
        
        const message = commitData.commit.message.split("\n")[0];
        const date = new Date(commitData.commit.author.date).toLocaleDateString();
        
        div.textContent = `${date}: ${message}`;
        container.appendChild(div);
    });
}

export function renderTasks(tasks) {
    const container = document.getElementById("tasks-list");
    if (!container) return;
    
    container.innerHTML = "";
    
    tasks.forEach(task => {
        const div = document.createElement("div");
        div.className = `task-item status-${task.status}`;
        div.textContent = `[${task.status}] ${task.title}`;
        container.appendChild(div);
    });
}