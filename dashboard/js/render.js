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

export function matchTaskToCommit(task, commits) {
    const match = commits.find(commitData => 
        commitData.commit.message.toLowerCase().includes(task.title.toLowerCase()) 
    );
    return match || null;
}

export function mergeTasks(tasks, commits) {
    return tasks.map(task => ({
        task: task,
        matchedCommit: matchTaskToCommit(task, commits)
    }));
}

export function renderTasks(tasks, commits) {
    const container = document.getElementById("tasks-list");
    if (!container) return;
    
    container.innerHTML = "";
    
    const mergedData = mergeTasks(tasks, commits);
    
    mergedData.forEach(item => {
        const taskDiv = document.createElement("div");
        taskDiv.className = `task-item status-${item.task.status.toLowerCase()}`;
        taskDiv.textContent = `[${item.task.status}] ${item.task.title}`;
        
        const ul = document.createElement("ul");
        const li = document.createElement("li");
        
        if (item.matchedCommit) {
            const date = new Date(item.matchedCommit.commit.author.date).toLocaleDateString();
            const msg = item.matchedCommit.commit.message.split("\n")[0];
            li.textContent = `${date} - ${msg}`;
        } else {
            li.textContent = "no matching activity yet.";
            li.style.color = "#757575";
            li.style.fontStyle = "italic";
        }
        
        ul.appendChild(li);
        taskDiv.appendChild(ul);
        container.appendChild(taskDiv);
    });
}