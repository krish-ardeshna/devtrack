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

export function renderTasks(tasks, commits) {
    const container = document.getElementById("tasks-list");
    if (!container) return;
    
    container.innerHTML = "";
    
    tasks.forEach(task => {
        const taskDiv = document.createElement("div");
        taskDiv.className = `task-item status-${task.status.toLowerCase()}`;
        taskDiv.textContent = `[${task.status}] #${task.id}: ${task.title}`;
        
        const relatedCommits = commits.filter(c => {
            const match = c.commit.message.match(/#(\d+)/);
            return match && parseInt(match[1]) === task.id;
        });
        
        if (relatedCommits.length > 0) {
            const ul = document.createElement("ul");
            relatedCommits.forEach(c => {
                const li = document.createElement("li");
                const date = new Date(c.commit.author.date).toLocaleDateString();
                const msg = c.commit.message.split("\n")[0];
                li.textContent = `${date} - ${msg}`;
                ul.appendChild(li);
            });
            taskDiv.appendChild(ul);
        }
        
        container.appendChild(taskDiv);
    });
}